# Generated by Django 4.2.4 on 2024-02-09 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_rename_user_id_appuser_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='is_sharer',
            field=models.BooleanField(default=False),
        ),
    ]
