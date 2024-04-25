from django.core.validators import MinLengthValidator
from django.db import models

from students.utils.validators import first_name_validator


class Person(models.Model):
    first_name = models.CharField(max_length=120, null=True, validators=[MinLengthValidator(2), first_name_validator])
    last_name = models.CharField(max_length=120, null=True, validators=[MinLengthValidator(2)])

    class Meta:
        abstract = True
