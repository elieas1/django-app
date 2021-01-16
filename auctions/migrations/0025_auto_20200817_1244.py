# Generated by Django 3.1 on 2020-08-17 19:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0024_auto_20200817_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bidding',
            name='bid',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='bidding',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 17, 12, 44, 27, 552610)),
        ),
        migrations.AlterField(
            model_name='listing',
            name='bid',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='listing',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 17, 12, 44, 27, 552610)),
        ),
    ]