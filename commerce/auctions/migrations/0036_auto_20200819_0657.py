# Generated by Django 3.1 on 2020-08-19 13:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0035_auto_20200819_0657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bidding',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 19, 6, 57, 40, 69035)),
        ),
        migrations.AlterField(
            model_name='listing',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 19, 6, 57, 40, 69035)),
        ),
    ]
