from django.contrib import admin
from .models import AccountUser
from django.contrib.auth.admin import UserAdmin


class AccountUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
            'Extra', {
                'fields': ('avatar', 'phone')
            }
        ),
    )


admin.site.register(AccountUser, AccountUserAdmin)