# Generated by Django 3.1.7 on 2021-03-23 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0015_auto_20210322_1353'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userorder',
            old_name='itemname',
            new_name='item',
        ),
    ]
