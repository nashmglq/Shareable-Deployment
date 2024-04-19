# Generated by Django 4.2.10 on 2024-03-11 11:38

import django.core.validators
from django.db import migrations, models
import sharer.models


class Migration(migrations.Migration):

    dependencies = [
        ('sharer', '0047_sharerupload_file_sharerupload_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sharerupload',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to=sharer.models.upload_video, validators=[django.core.validators.FileExtensionValidator(['mp4'])]),
        ),
    ]