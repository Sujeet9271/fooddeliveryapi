# Generated by Django 3.1.7 on 2021-04-16 06:53

from django.db import migrations, models
import order.models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0047_auto_20210416_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.TextField(default=order.models.user_address),
        ),
        migrations.AlterField(
            model_name='order',
            name='contact_number',
            field=models.CharField(default=order.models.user_contact, max_length=10),
        ),
    ]
