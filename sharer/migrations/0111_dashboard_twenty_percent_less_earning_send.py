# Generated by Django 5.0.3 on 2024-03-28 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sharer', '0110_remove_dashboard_twenty_percent_cut_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashboard',
            name='twenty_percent_less_earning_send',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
