# Generated by Django 3.1.7 on 2021-04-16 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0007_auto_20210417_0018'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='rating_average',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='review_count',
            field=models.IntegerField(default=0),
        ),
    ]
