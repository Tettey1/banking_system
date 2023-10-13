from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from Managers.models import Managers
from Managers.tasks import send_user_password
from Managers.utils import create_random_password
from django.conf import settings
from Managers.models import Roles
from django.db.utils import IntegrityError
import json
from Managers.models import Permission
from Managers.decorators import check_permission


@csrf_exempt
@require_POST
@check_permission('add_user')
def create_staff(request):
    try:
        data = json.loads(request.body)
        email = data.get("email")
        staff_id = data.get("staff_id")
        phone_number = data.get("phone_number")
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        role_names = data.get("role_name")

        if any(
                item == "" for item in
            [email, staff_id, phone_number, first_name, last_name, role_names
             ]) is None:
            return JsonResponse(
                {
                    "message": "Missing parameters in request",
                    "status": 400,
                },
                status=400,
            )

        if not isinstance(role_names, list):
            role_names = [role_names]

        role_ids = Roles.objects.values_list("id", flat=True)
        invalid_roles = [
            role_id for role_id in role_names if role_id not in role_ids
        ]
        if len(invalid_roles) > 0:
            return JsonResponse(
                {
                    "message":
                    "Invalid role ID(s): " +
                    ", ".join(map(str, invalid_roles)),
                    "status":
                    400,
                },
                status=400,
            )
        roles = Roles.objects.filter(id__in=role_names)

        user, created = Managers.objects.get_or_create(
            email=email,
            defaults={
                "first_name": first_name,
                "last_name": last_name,
                "staff_id": staff_id,
                "phone_number": phone_number
            },
        )

        if not created:
            return JsonResponse(
                {
                    "message": "User not created / already exists",
                    "status": 400
                },
                status=400,
            )

        password = create_random_password()
        user.set_password(password)
        user.save()

        user.roles.set(roles)
        if settings.IT_MANAGER_ROLE in roles:
            permissions = Permission.objects.all().exclude(name=['add_customer', 'transaction', 'view'])
            user.user_permissions.set(permissions)
        elif settings.TELLER_ROLE in roles:
            permissions = Permission.objects.all().exclude(name='add_user')
            user.user_permissions.set(permissions)

        elif settings.MANAGER_ROLE in roles:
            permissions = Permission.objects.all().exclude(name='add_user')
            user.user_permissions.set(permissions)

        send_user_password.delay(password=password, email=email)
        message = "Please check your email for your credentials"

        response_data = {
            "message": message,
            "status": 200,
            "data": {
                "profile_id":
                user.profile_id,
                "email":
                user.email,
                "first_name":
                user.first_name,
                "last_name":
                user.last_name,
                "staff_id":
                user.staff_id,
                "phone_number":
                user.phone_number,
                "role": [role.name for role in user.roles.all()]
                if user.roles.exists() else None,
            },
        }

        return JsonResponse(response_data, content_type="application/json")

    except json.JSONDecodeError:
        return JsonResponse(
            {
                "message":
                "JSONDecodeError, You might have forgotten to provide your data/field(s) in JSON format.",
                "status": 400,
            },
            status=400,
        )
    except IntegrityError as e:
        return JsonResponse(
            {
                "message": "Service ID already exists",
                "status": 400
            },
            status=400)
    except Exception as e:
        return JsonResponse(
            {
                "message": "An error occurred: " + str(e),
                "status": 500
            },
            status=500)
