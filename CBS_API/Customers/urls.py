from django.urls import path
from Customers.api_views.user_setup import create_customer
from Customers.api_views.customers import list_customers
from Customers.api_views.customer_details import customer_details

app_name = 'customers'
urlpatterns = [
    path('create-customer/', create_customer, name='create-customer'),
    path('list-customers/', list_customers, name='list-customers'),
    path('customer-details/', customer_details, name='customer-details'),
]
