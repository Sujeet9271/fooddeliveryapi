# Generated by Django 3.1.7 on 2021-03-23 05:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_auto_20210322_1416'),
        ('menu', '0003_auto_20210323_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='restaurant.restaurant'),
        ),
        migrations.AlterField(
            model_name='sub_category',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_category', to='menu.category'),
        ),
    ]
