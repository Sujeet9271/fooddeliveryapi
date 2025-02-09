# Generated by Django 3.1.7 on 2021-04-13 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20210413_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='address',
            field=models.TextField(default='', help_text='Address'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='contact_number',
            field=models.PositiveIntegerField(help_text='Contact phone number for food delivery'),
        ),
    ]
