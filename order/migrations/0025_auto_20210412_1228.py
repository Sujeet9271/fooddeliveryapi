# Generated by Django 3.1.7 on 2021-04-12 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0024_auto_20210409_1158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='price',
        ),
        migrations.AlterField(
            model_name='order',
            name='user_order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='order.userorder'),
        ),
    ]
