# Generated by Django 5.1 on 2024-08-16 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_posts_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='banner',
            field=models.ImageField(blank=True, default='fallback.jpeg', upload_to=''),
        ),
    ]
