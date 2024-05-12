import pycountry

from django.contrib.auth import get_user_model
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from user_account.managers import PeopleManager


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


