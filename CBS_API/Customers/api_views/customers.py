from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from Managers.decorators import check_permission
from Customers.models import Customers
from accounts.models import Accounts

# @csrf_exempt
# @check_permission("view")
# def list_customers(request):
#     customers = Customers.objects.all().values(
#         "profile_id", "email", "first_name", "last_name", "mobile_number",
#         "city", "postal_address", "sex", "marital_status", "occupation",
#         "ghana_card_number", "date_of_birth", "accounts__account_number")

#     response_data = {
#         "message": "customers listed successfully",
#         "status": 200,
#         "data": list(customers),
#     }

#     return JsonResponse(response_data, safe=False)


@csrf_exempt
@check_permission("view")
def list_customers(request):
    customers = Accounts.objects.all().values(
        "user__profile_id", "user__email", "user__first_name",
        "user__last_name", "user__mobile_number", "user__city",
        "user__postal_address", "user__sex", "user__marital_status",
        "user__occupation", "user__ghana_card_number", "user__date_of_birth",
        "account_number", "amount")

    response_data = {
        "message": "customers listed successfully",
        "status": 200,
        "data": list(customers),
    }

    return JsonResponse(response_data, safe=False)
