from django.urls import path
from transactions.api_views.deposit import create_transaction
from transactions.api_views.transactions import list_transactions
from withdrawals.api_views.withdrawal import create_withdrawal

app_name = 'transactions'
urlpatterns = [
    path('transact/', create_transaction, name='transact'),
    path('transactions/', list_transactions, name='transactions'),
    path('withdrawal/', create_withdrawal, name='withdrawal'),
]
