# Generated by Django 3.1 on 2020-08-19 13:53

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0030_auto_20200818_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bidding',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 19, 6, 52, 54, 748040)),
        ),
        migrations.AlterField(
            model_name='listing',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 19, 6, 52, 54, 747042)),
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='listing_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rewatch', to='auctions.listing'),
        ),
    ]