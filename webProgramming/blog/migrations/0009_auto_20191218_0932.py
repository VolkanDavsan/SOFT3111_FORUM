# Generated by Django 3.0 on 2019-12-18 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_news_img2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='img1',
        ),
        migrations.RemoveField(
            model_name='news',
            name='img2',
        ),
    ]