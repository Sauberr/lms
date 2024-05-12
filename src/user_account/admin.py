from django.contrib import admin

from user_account.models import UserProfile, ProxyUser

admin.site.register([ProxyUser, UserProfile])


