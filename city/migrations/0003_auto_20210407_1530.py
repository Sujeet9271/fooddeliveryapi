# Generated by Django 3.1.7 on 2021-04-07 09:45

import city.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0002_city_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=city.models.location),
        ),
    ]
