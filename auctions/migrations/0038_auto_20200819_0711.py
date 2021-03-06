# Generated by Django 3.1 on 2020-08-19 14:11

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0037_auto_20200819_0658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bidding',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 19, 7, 10, 58, 918024)),
        ),
        migrations.AlterField(
            model_name='listing',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 19, 7, 10, 58, 918024)),
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='listing_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rewatch', to='auctions.listing'),
        ),
    ]
