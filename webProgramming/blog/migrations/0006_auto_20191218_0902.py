# Generated by Django 3.0 on 2019-12-18 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20191217_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image1',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='news',
            name='image2',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]