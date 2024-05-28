# Generated by Django 4.2 on 2024-05-28 17:44

from django.db import migrations, models
import shortuuid.django_fields
import students.utils.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Group",
            fields=[
                (
                    "id",
                    shortuuid.django_fields.ShortUUIDField(
                        alphabet="abcdefghijklmnopqrstuvwxyz12345678090",
                        length=10,
                        max_length=30,
                        prefix="group_",
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("title", models.CharField(max_length=120)),
                ("department", models.CharField(max_length=120)),
                ("students_count", models.PositiveIntegerField(default=0)),
                ("description", models.TextField(null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "gpa",
                    models.FloatField(
                        default=0,
                        null=True,
                        validators=[students.utils.validators.gpa_validator],
                    ),
                ),
                (
                    "median_age",
                    models.FloatField(
                        default=0,
                        null=True,
                        validators=[students.utils.validators.median_age_validator],
                    ),
                ),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "max_count_of_students",
                    models.PositiveIntegerField(default=20, null=True),
                ),
            ],
            options={
                "verbose_name": "Group",
                "verbose_name_plural": "Groups",
            },
        ),
    ]
