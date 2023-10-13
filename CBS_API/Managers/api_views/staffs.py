from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from Managers.models import Managers
from Managers.decorators import check_permission


@csrf_exempt
@check_permission("view")
def list_staffs(request):

    staffs = Managers.objects.all().values("profile_id", "email", "first_name",
                                        "last_name", "roles__name",
                                        "phone_number", "staff_id")

    staff_list = []

    for staff_data in staffs:
        staff_instance = Managers.objects.get(
            profile_id=staff_data["profile_id"])  # Fetch the staff instance
        roles = [role.name for role in staff_instance.roles.all()
                 ]  # Retrieve roles for this staff instance
        staff_data["role__name"] = roles
        staff_list.append(staff_data)

    response_data = {
        "message": "Staff listed successfully",
        "status": 200,
        "data": staff_list,
    }

    return JsonResponse(response_data, safe=False)
