from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User, Group
from .models import Costumer


# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class CustomerInline(admin.StackedInline):
    model = Costumer
    can_delete = False
    verbose_name_plural = 'customers'


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (CustomerInline,)


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
admin.site.register(Costumer)
