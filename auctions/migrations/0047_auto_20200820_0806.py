# Generated by Django 3.1 on 2020-08-20 15:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0046_auto_20200819_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='edited',
            field=models.TextField(default='False'),
        ),
        migrations.AlterField(
            model_name='bidding',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 20, 8, 6, 28, 880727)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 20, 8, 6, 28, 880727)),
        ),
        migrations.AlterField(
            model_name='listing',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 20, 8, 6, 28, 879726)),
        ),
    ]
