# Generated by Django 4.2 on 2024-04-25 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("groups", "0001_initial"),
        ("teachers", "0002_alter_teacher_options_alter_teacher_sex"),
    ]

    operations = [
        migrations.AddField(
            model_name="teacher",
            name="group",
            field=models.ManyToManyField(to="groups.group"),
        ),
    ]