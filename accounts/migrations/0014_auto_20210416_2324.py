# Generated by Django 3.1.7 on 2021-04-16 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='contact_number',
            field=models.CharField(default='', max_length=10),
        ),
    ]
