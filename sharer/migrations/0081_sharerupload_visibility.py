# Generated by Django 4.2.10 on 2024-03-19 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sharer', '0080_remove_rating_has_rated'),
    ]

    operations = [
        migrations.AddField(
            model_name='sharerupload',
            name='visibility',
            field=models.CharField(choices=[('ALL', 'All (followers and non-followers)'), ('FOLLOWERS', 'Followers only'), ('NON_FOLLOWERS', 'Non-followers only')], default='ALL', max_length=20),
        ),
    ]
