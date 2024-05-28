from django.db import models
from faker import Faker
from shortuuid.django_fields import ShortUUIDField

from students.utils.validators import gpa_validator, median_age_validator


class Group(models.Model):
    id = ShortUUIDField(
        unique=True,
        length=10,
        max_length=30,
        prefix="group_",
        alphabet="abcdefghijklmnopqrstuvwxyz12345678090",
        primary_key=True,
    )
    title = models.CharField(max_length=120)
    department = models.CharField(max_length=120)
    students_count = models.PositiveIntegerField(default=0)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    gpa = models.FloatField(default=0, null=True, validators=[gpa_validator])
    median_age = models.FloatField(default=0, null=True, validators=[median_age_validator])
    updated_at = models.DateTimeField(auto_now=True)
    max_count_of_students = models.PositiveIntegerField(default=20, null=True)

    def __str__(self):
        return f"{self.title} [{self.department}] ({self.id})"

    class Meta:
        verbose_name = "Group"
        verbose_name_plural = "Groups"

    @classmethod
    def generate_instances(cls, count):
        faker = Faker()
        for _ in range(count):
            department = faker.job()
            start_date = faker.date_time_between(start_date="-4y")
            start_year = start_date.year
            cls.objects.create(
                title=f"{department[0]}-{start_year}",
                department=department,
                description=faker.text(max_nb_chars=200),
                students_count=faker.random.randint(1, 50),
                gpa=round(faker.random.uniform(1, 5), 2),
                median_age=round(faker.random.uniform(18, 30), 2),
                created_at=faker.date_time_between(start_date="-30y", end_date="-18y"),
                updated_at=faker.date_time_between(start_date="-30y", end_date="-18y"),
            )
