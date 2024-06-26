# Generated by Django 5.0.3 on 2024-03-30 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sharer', '0112_remove_dashboard_twenty_percent_less_earning_send'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sharer',
            name='category',
            field=models.CharField(choices=[('', 'Not specified'), ('Art', 'Art'), ('Comics', 'Comics'), ('Writing', 'Writing'), ('Music', 'Music'), ('Podcasts', 'Podcasts'), ('Video & Film', 'Video & Film'), ('Photography', 'Photography'), ('Crafts & DIY', 'Crafts & DIY'), ('Dance & Theater', 'Dance & Theater'), ('Gaming', 'Gaming'), ('Education', 'Education'), ('Science', 'Science'), ('Technology', 'Technology'), ('Health & Fitness', 'Health & Fitness'), ('Lifestyle', 'Lifestyle'), ('Fashion & Beauty', 'Fashion & Beauty'), ('Food & Cooking', 'Food & Cooking'), ('Travel & Outdoor', 'Travel & Outdoor'), ('Business & Entrepreneurship', 'Business & Entrepreneurship'), ('Parenting & Family', 'Parenting & Family')], default='', max_length=30),
        ),
    ]
