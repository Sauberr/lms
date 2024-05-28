from django.utils import timezone
import pycountry

from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from django.utils.translation import gettext_lazy as _

from user_account.managers import PeopleManager, CustomerManager

STATUS_CHOICES = (
    ("Student", "Student"),
    ("Teacher", "Teacher"),
    ("Mentor", "Mentor"),
)

SEX_CHOICES = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Undefined", "I don't want to tell"),
)

COUNTRY_CHOICES = [(f"{country.name}", f"{country.name}") for country in pycountry.countries]


class Customer(AbstractBaseUser, PermissionsMixin):

    username_validator = UnicodeUsernameValidator()

    first_name = models.CharField(_("name"), max_length=150, blank=True)
    last_name = models.CharField(_("surname"), max_length=150, blank=True)
    email = models.EmailField(_("email address"), blank=True, null=True)
    phone_number = PhoneNumberField(_("phone number"), blank=True, null=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    birth_date = models.DateField(_("birth date"), blank=True, null=True)
    avatar = models.ImageField(_("avatar"), upload_to="avatars/", blank=True, null=True)

    objects = CustomerManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def get_working_time(self):
        return f"Time on site: {timezone.now() - self.date_joined}"


class ProxyUser(get_user_model()):
    people = PeopleManager()

    class Meta:
        proxy = True
        ordering = ("-pk",)
        verbose_name = "Proxy User"
        verbose_name_plural = "Proxy Users"

    def do_something(self):
        print(f'{self.first_name}')


class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    pk = user.primary_key
    photo = models.ImageField(upload_to="user_photos", blank=True, null=True)
    phone_number = PhoneNumberField(null=True)
    location = models.CharField(max_length=44, choices=COUNTRY_CHOICES, default="Undefined")
    birth_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=7, choices=STATUS_CHOICES, default="Student")
    sex = models.CharField(max_length=9, choices=SEX_CHOICES, default="Undefined")

    def __str__(self):
        return f'{self.user} {self.status}'

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"


