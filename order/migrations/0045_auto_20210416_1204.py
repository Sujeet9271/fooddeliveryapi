# Generated by Django 3.1.7 on 2021-04-16 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0044_auto_20210414_1128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userorder',
            name='deliver_to',
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='contact_number',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.DeleteModel(
            name='Delivery',
        ),
    ]
