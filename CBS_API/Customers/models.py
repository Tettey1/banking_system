from django.db import models
from Managers.utils import generate_profile_id


class Customers(models.Model):
    class MaritalStatus(models.TextChoices):
        SINGLE = "SINGLE"
        MARRIED = "MARRIED"

    class Sex(models.TextChoices):
        MALE = "MALE"
        FEMALE = "FEMALE"

    profile_id = models.CharField(max_length=255,
                                  default=generate_profile_id,
                                  blank=True,
                                  null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    ghana_card_number = models.CharField(max_length=255, blank=True, null=True, unique=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    mobile_number = models.CharField(max_length=255, blank=True, null=True)
    occupation = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    postal_address = models.CharField(max_length=255, blank=True, null=True)
    marital_status = models.CharField(max_length=255,
                                      blank=True,
                                      null=True,
                                      choices=MaritalStatus.choices,
                                      default=MaritalStatus.SINGLE)
    sex = models.CharField(max_length=255,
                           blank=True,
                           null=True,
                           choices=Sex.choices,
                           default=Sex.MALE)

    def __str__(self):
        return self.first_name
