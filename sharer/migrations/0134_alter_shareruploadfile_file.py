# Generated by Django 5.0.3 on 2024-04-15 10:22

import django.core.validators
import sharer.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sharer', '0133_alter_shareruploadfile_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shareruploadfile',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=sharer.models.upload_file, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['txt', 'pdf', 'doc', 'docx'])]),
        ),
    ]
