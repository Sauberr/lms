# Generated by Django 4.2 on 2024-04-21 13:15

import django.core.validators
from django.db import migrations, models

import students.utils.validators


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="student",
            options={"verbose_name": "Student", "verbose_name_plural": "Students"},
        ),
        migrations.AlterField(
            model_name="student",
            name="first_name",
            field=models.CharField(
                max_length=120,
                null=True,
                validators=[
                    django.core.validators.MinLengthValidator(2),
                    students.utils.validators.first_name_validator,
                ],
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="last_name",
            field=models.CharField(
                max_length=120,
                null=True,
                validators=[django.core.validators.MinLengthValidator(2)],
            ),
        ),
    ]
