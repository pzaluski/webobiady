from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import UserProfile


class UserProfileAdmin(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Informacje dodatkowe'
    verbose_name = "Informacje"


class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileAdmin, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
