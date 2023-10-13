from django.db import models
from Customers.models import Customers
from accounts.utils import generate_account_number


class Accounts(models.Model):
    user = models.OneToOneField(Customers,
                                on_delete=models.CASCADE,
                                primary_key=True)
    account_number = models.CharField(max_length=255,
                                      default=generate_account_number,
                                      blank=True,
                                      null=True)
    amount = models.FloatField(default=0.0, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user.first_name
