from django.urls import path
from accounts.api_views.account import list_accounts

app_name = 'accounts'
urlpatterns = [
    path('accounts/', list_accounts, name='accounts'),
]
