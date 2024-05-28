# Generated by Django 4.2 on 2024-05-23 13:07

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ("user_account", "0002_userprofile"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="phone_number",
            field=phonenumber_field.modelfields.PhoneNumberField(
                blank=True,
                max_length=128,
                null=True,
                region=None,
                verbose_name="phone number",
            ),
        ),
        migrations.AlterField(
            model_name="customer",
            name="email",
            field=models.EmailField(
                blank=True, max_length=254, null=True, verbose_name="email address"
            ),
        ),
    ]
