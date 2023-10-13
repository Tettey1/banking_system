from django.contrib import admin
from Managers.models import Managers, Roles, Permission
# Register your models here.

admin.site.register(Managers)
admin.site.register(Roles)
admin.site.register(Permission)
