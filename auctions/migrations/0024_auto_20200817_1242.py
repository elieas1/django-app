# Generated by Django 3.1 on 2020-08-17 19:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0023_auto_20200817_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bidding',
            name='bid',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bidding',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 17, 12, 42, 2, 618315)),
        ),
        migrations.AlterField(
            model_name='listing',
            name='bid',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 17, 12, 42, 2, 618315)),
        ),
    ]
