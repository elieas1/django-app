# Generated by Django 3.1 on 2020-08-19 16:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0040_auto_20200819_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bidding',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 19, 9, 46, 45, 234099)),
        ),
        migrations.AlterField(
            model_name='listing',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 19, 9, 46, 45, 233100)),
        ),
    ]
