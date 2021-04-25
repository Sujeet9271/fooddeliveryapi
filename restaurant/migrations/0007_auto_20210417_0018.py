# Generated by Django 3.1.7 on 2021-04-16 18:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurant', '0006_auto_20210416_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantrating',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='restaurant.restaurant'),
        ),
        migrations.AlterUniqueTogether(
            name='restaurantrating',
            unique_together={('user', 'restaurant')},
        ),
    ]
