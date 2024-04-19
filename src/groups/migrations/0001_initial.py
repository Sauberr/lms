# Generated by Django 4.2 on 2024-04-18 15:59

from django.db import migrations, models
import django_ckeditor_5.fields
import shortuuid.django_fields


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
                (
                    "description",
                    django_ckeditor_5.fields.CKEditor5Field(blank=True, default="Description of the group", null=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "Group",
            },
        ),
    ]
