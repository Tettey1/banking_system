from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db.utils import IntegrityError
import json
from Managers.decorators import check_permission
from Customers.models import Customers


@csrf_exempt
@require_POST
@check_permission('add_customer')
def create_customer(request):
    try:
        data = json.loads(request.body)
        email = data.get("email")
        mobile_number = data.get("mobile_number")
        occupation = data.get("occupation")
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        ghana_card_number = data.get("ghana_card_number")
        date_of_birth = data.get("date_of_birth")
        city = data.get("city")
        postal_address = data.get("postal_address")
        sex = data.get("sex")
        marital_status = data.get("marital_status")

        if any(item == "" for item in [
                mobile_number, occupation, first_name, last_name,
                ghana_card_number, date_of_birth, city, postal_address, sex,
                marital_status
        ]) is None:
            return JsonResponse(
                {
                    "message": "Missing parameters in request",
                    "status": 400,
                },
                status=400,
            )

        if Customers.objects.filter(email=email).exists():
            return JsonResponse(
                {
                    "message": "User already exists",
                    "status": 400,
                },
                status=400,
            )

        if Customers.objects.filter(
                ghana_card_number=ghana_card_number).exists():
            return JsonResponse(
                {
                    "message": "Ghana card number already exists",
                    "status": 400,
                },
                status=400,
            )

        user, created = Customers.objects.get_or_create(
            email=email,
            defaults={
                "first_name": first_name,
                "last_name": last_name,
                "occupation": occupation,
                "mobile_number": mobile_number,
                "ghana_card_number": ghana_card_number,
                "date_of_birth": date_of_birth,
                "city": city,
                "postal_address": postal_address,
                "sex": sex,
                "marital_status": marital_status
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

        user.save()

        message = "User created successfully"

        response_data = {
            "message": message,
            "status": 200,
            "data": {
                "profile_id": user.profile_id,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "ghana_card_number": user.ghana_card_number,
                "mobile_number": user.mobile_number,
                "occupation": user.occupation,
                "date_of_birth": user.date_of_birth,
                "city": user.city,
                "postal_address": user.postal_address,
                "sex": user.sex,
                "marital_status": user.marital_status
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
                "message": "User not created / already exists",
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
