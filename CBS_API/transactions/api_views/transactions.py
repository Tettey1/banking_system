from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from Managers.decorators import check_permission
from transactions.models import Transactions


@csrf_exempt
@check_permission("view")
def list_transactions(request):
    transactions = Transactions.objects.all().values(
        "user__first_name", "amount", "account_number", "teller_id", "date_created",
        "transaction_id", "transaction_type")

    response_data = {
        "message": "transactions listed successfully",
        "status": 200,
        "data": list(transactions),
    }

    return JsonResponse(response_data, safe=False)
