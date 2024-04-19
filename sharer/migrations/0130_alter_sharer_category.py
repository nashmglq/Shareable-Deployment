# Generated by Django 5.0.3 on 2024-04-14 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sharer', '0129_alter_sharer_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sharer',
            name='category',
            field=models.CharField(choices=[('Not specified', 'Not specified'), ('Art', 'Art'), ('Comics', 'Comics'), ('Writing', 'Writing'), ('Music', 'Music'), ('Podcasts', 'Podcasts'), ('Video & Film', 'Video & Film'), ('Photography', 'Photography'), ('Crafts & DIY', 'Crafts & DIY'), ('Dance & Theater', 'Dance & Theater'), ('Gaming', 'Gaming'), ('Education', 'Education'), ('Science', 'Science'), ('Technology', 'Technology'), ('Health & Fitness', 'Health & Fitness'), ('Lifestyle', 'Lifestyle'), ('Fashion & Beauty', 'Fashion & Beauty'), ('Food & Cooking', 'Food & Cooking'), ('Travel & Outdoor', 'Travel & Outdoor'), ('Business & Entrepreneurship', 'Business & Entrepreneurship'), ('Parenting & Family', 'Parenting & Family'), ('Manga', 'Manga'), ('Sports', 'Sports')], default='Not specified', max_length=30),
        ),
    ]