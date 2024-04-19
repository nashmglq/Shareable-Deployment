# Generated by Django 4.2.10 on 2024-03-17 01:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0025_remove_appuser_otp_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='username',
            field=models.CharField(default=1, max_length=50, validators=[django.core.validators.MinLengthValidator(4)]),
            preserve_default=False,
        ),
    ]
