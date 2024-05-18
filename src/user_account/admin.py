from django.contrib import admin
from django.contrib.auth import get_user_model

from user_account.models import ProxyUser, UserProfile

admin.site.register([ProxyUser, UserProfile, get_user_model()])


