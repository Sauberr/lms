from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from faker import Faker
from shortuuid.django_fields import ShortUUIDField


class Group(models.Model):
    id = ShortUUIDField(unique=True, length=10, max_length=30, prefix='group_', alphabet='abcdefghijklmnopqrstuvwxyz12345678090')
    title = models.CharField(max_length=120)
    department = models.CharField(max_length=120)
    students_count = models.PositiveIntegerField(default=0)
    description = CKEditor5Field(config_name='extends', blank=True, null=True, default='Description of the group')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} [{self.department}] ({self.id})"

    @classmethod
    def generate_instances(cls, count):
        faker = Faker()
        for _ in range(count):
            department = faker.job()
            start_date = faker.date_time_between(start_date="-4y")
            start_year = start_date[4]
            cls.objects.create(
                title=f"{department[0]}-{start_year}",
                department=department,
                description=faker.text(max_nb_chars=200),
                students_count=faker.random.randint(1, 50),
                created_at=faker.date_time_between(start_date='-30y', end_date='-18y'),
                updated_at=faker.date_time_between(start_date='-30y', end_date='-18y'),
            )


