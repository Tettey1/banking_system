from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from Managers.decorators import check_permission
from Customers.models import Customers
from accounts.models import Accounts
import json


@csrf_exempt
@require_POST
@check_permission("view")
def customer_details(request):

    try:
        data = json.loads(request.body)
        profile_id = data.get("profile_id")

        if profile_id == "":
            return JsonResponse(
                {
                    "message": "Profile id is required.",
                    "status": 400
                },
                status=400)

        profile = Customers.objects.get(profile_id=profile_id)
        account = Accounts.objects.get(user=profile)

        message = "Customer details found"
        response_data = {
            "message": message,
            "status": 200,
            "data": {
                "profile_id": profile.profile_id,
                "email": profile.email,
                "first_name": profile.first_name,
                "last_name": profile.last_name,
                "ghana_card_number": profile.ghana_card_number,
                "phone_number": profile.mobile_number,
                "occupation": profile.occupation,
                "date_of_birth": profile.date_of_birth,
                "city": profile.city,
                "postal_address": profile.postal_address,
                "sex": profile.sex,
                "marital_status": profile.marital_status,
                "account_number": account.account_number
            },
        }

        return JsonResponse(response_data, safe=False)

    except json.JSONDecodeError:
        return JsonResponse(
            {
                "message":
                "JSONDecodeError, You might have forgotten to provide your data / field(s) in json format.",
                "status": 400,
            },
            status=400,
        )

    except Customers.DoesNotExist:
        return JsonResponse(
            {
                "message": "Customer details not found",
                "status": 404,
            },
            status=404,
        )

    except Accounts.DoesNotExist:
        return JsonResponse(
            {
                "message": "Account details not found",
                "status": 404,
            }
        )
