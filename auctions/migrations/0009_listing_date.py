# Generated by Django 3.1 on 2020-08-17 14:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_auto_20200817_0653'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 17, 7, 3, 26, 666358)),
        ),
    ]