# Generated by Django 5.0.1 on 2024-02-17 04:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sharer', '0003_sharer_follows'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sharer',
            name='follows',
        ),
    ]
