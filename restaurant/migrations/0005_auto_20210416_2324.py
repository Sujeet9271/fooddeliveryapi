# Generated by Django 3.1.7 on 2021-04-16 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_restaurant_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='phnumber',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
