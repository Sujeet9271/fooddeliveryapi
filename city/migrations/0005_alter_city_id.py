# Generated by Django 3.2 on 2021-04-28 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0004_auto_20210416_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
