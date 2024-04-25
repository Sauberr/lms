import random

from django.db import models
from faker import Faker

from groups.models import Group

from abstract_class.models import Person


SEX_CHOICE = {("M", "Man"), ("W", "Woman")}


class Teacher(Person):
    age = models.IntegerField(default=0)
    experience = models.PositiveIntegerField(default=0)
    salary = models.PositiveIntegerField(default=0)
    sex = models.CharField(choices=SEX_CHOICE, max_length=1)
    subject = models.CharField(max_length=255)
    group = models.ManyToManyField(Group)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"

    @classmethod
    def generate_instances(cls, count):
        faker = Faker()
        for _ in range(count):
            cls.objects.create(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                age=random.randint(25, 65),
                experience=random.randint(0, 40),
                salary=random.randint(500, 2500),
            )
