from datetime import datetime

from django.db import models
from faker import Faker

from abstract_class.models import Person

from groups.models import Group

from uuid import uuid4


class Student(Person):
    uuid = models.UUIDField(primary_key=True, editable=False, default=uuid4, unique=True, db_index=True)
    email = models.EmailField(max_length=120)
    grade = models.PositiveIntegerField(default=0)
    birth_date = models.DateField(null=True)
    department = models.CharField(max_length=120, null=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def age(self):
        return datetime.now().year - self.birth_date.year

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    @classmethod
    def generate_instances(cls, count):
        faker = Faker()
        for _ in range(count):
            student = cls.objects.create( # noqa
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                email=faker.email(),
                birth_date=faker.date_time_between(start_date="-30y", end_date="-18y"),
                grade=faker.random_int(min=1, max=12),
                department=faker.job(),
            )
