# Generated by Django 3.1 on 2020-08-19 19:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0044_auto_20200819_0951'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 19, 12, 19, 39, 755212)),
        ),
        migrations.AlterField(
            model_name='bidding',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 19, 12, 19, 39, 754214)),
        ),
        migrations.AlterField(
            model_name='listing',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 19, 12, 19, 39, 753217)),
        ),
    ]
