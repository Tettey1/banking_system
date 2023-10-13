from django.db import models
from Customers.models import Customers


class Withdrawals(models.Model):
    user = models.ForeignKey(Customers,
                             on_delete=models.CASCADE,
                             related_name="withdrawals")
    amount = models.FloatField(default=0.0, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name
