from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from Managers.decorators import check_permission
from accounts.models import Accounts


@csrf_exempt
@check_permission("view")
def list_accounts(request):
    accounts = Accounts.objects.all().values("user__first_name",
                                             "user__last_name", "amount",
                                             "account_number", "date_created")

    response_data = {
        "message": "transactions listed successfully",
        "status": 200,
        "data": list(accounts),
    }

    return JsonResponse(response_data, safe=False)
