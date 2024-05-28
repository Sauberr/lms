from django.apps import AppConfig
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, pre_save


class UserAccountConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "user_account"

    def ready(self):
        from user_account.services.signals import create_user_profile_signal, pre_save_user_signal

        post_save.connect(create_user_profile_signal, sender=get_user_model())
        pre_save.connect(pre_save_user_signal, sender=get_user_model())
