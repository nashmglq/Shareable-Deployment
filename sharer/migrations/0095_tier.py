# Generated by Django 4.2.10 on 2024-03-25 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sharer', '0094_alter_rating_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tier_level', models.IntegerField(choices=[(1, 'Bronze'), (2, 'Silver'), (3, 'Gold')])),
            ],
        ),
    ]
