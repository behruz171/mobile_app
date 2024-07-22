from django.contrib import admin
from .models import *

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'birth_date', 'pin_code')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'birth_date', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'birth_date', 'is_staff')
    search_fields = ('email', 'first_name')
    ordering = ('email',)

admin.site.register(User, UserAdmin)
admin.site.register(EmailVerification)