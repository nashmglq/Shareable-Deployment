# Generated by Django 4.2.4 on 2024-02-23 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sharer', '0030_alter_sharer_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sharer',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
