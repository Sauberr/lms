from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ("email", "first_name", "last_name", "password1", "password2")

    def clean(self):
        _cleaned_data = super().clean()
        if not bool(_cleaned_data["email"]) and not bool(_cleaned_data["phone_number"]):
            raise ValidationError("You must provide either an email or a phone number")

        elif not bool(_cleaned_data["email"]):
            if get_user_model().objects.filter(phone_number=_cleaned_data['phone_number']).exists():
                raise ValidationError("User with this phone number already exists")

        elif not bool(_cleaned_data["phone_number"]):
            if get_user_model().objects.filter(email=_cleaned_data['email']).exists():
                raise ValidationError("User with this email already exists")

        return _cleaned_data

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        special_characters = "!@#$%^&*()_-+={}[]|\:;'<>?,./"
        capitalize_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        has_special = any(char in special_characters for char in password1)
        has_capital = any(char in capitalize_letters for char in password1)

        if not has_special and not has_capital:
            raise ValidationError("Password must contain at least one special character and one uppercase letter")
        elif not has_special:
            raise ValidationError("Password must contain at least one special character")
        elif not has_capital:
            raise ValidationError("Password must contain at least one uppercase letter")

        return password1

