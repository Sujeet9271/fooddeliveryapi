# Generated by Django 3.2 on 2021-04-28 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(1, 'Pending'), (2, 'Received'), (3, 'In the Kitchen'), (4, 'Out for Delivery'), (5, 'Delivered')], default=1),
        ),
    ]
