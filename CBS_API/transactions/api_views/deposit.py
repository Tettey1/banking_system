from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db.utils import IntegrityError
import json
from Managers.decorators import check_permission
from transactions.decorators import is_teller
from Customers.models import Customers
from accounts.models import Accounts
from transactions.models import Transactions
from deposits.models import Deposits


@csrf_exempt
@require_POST
@check_permission('transaction')
@is_teller
def create_transaction(request, teller=None):
    try:
        data = json.loads(request.body)
        amount = data.get("amount")
        account_number = data.get("account_number")

        if any(item == "" for item in [
                amount,account_number
        ]) is None:
            return JsonResponse(
                {
                    "message": "Missing parameters in request",
                    "status": 400,
                },
                status=400,
            )

        # get the account
        try:
            account = Accounts.objects.get(account_number=account_number)
            transaction = Transactions.objects.create(
                user=account.user,
                amount=amount,
                teller_id=teller.profile_id,
                account_number=account_number
            )
            deposit = Deposits.objects.create(
                user=account.user
            )
            deposit.amount += amount
            deposit.save()
            account.amount += amount
            account.save()

        except Accounts.DoesNotExist:
            return JsonResponse(
                {
                    "message": "Account does not exist",
                    "status": 400,
                },
                status=400,
            )

        return JsonResponse(
            {
                "message": f"Transaction created successfully for {account_number} account for {amount} amount",
                "status": 200
            }
        )

        return JsonResponse(
            {
                "message": "Transaction already exists",
                "status": 400,
            },
            status=400,
        )

    except json.decoder.JSONDecodeError:
        return JsonResponse(
            {
                "message": "Invalid JSON",
                "status": 400,
            },
            status=400,
        )
