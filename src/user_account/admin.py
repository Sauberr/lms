from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from user_account.models import ProxyUser, UserProfile


admin.site.register([ProxyUser, UserProfile])


class ProfileAdmin(admin.StackedInline):
    model = UserProfile


@admin.register(get_user_model())
class CustomerAdmin(UserAdmin):
    inlines = [ProfileAdmin]
    fields = ('first_name', 'last_name', 'password', 'email', 'phone_number')
    list_display = ('first_name', 'last_name', 'email')
    fieldsets = None
    ordering = ('email',)
    readonly_fields = ('email',)

