# Generated by Django 3.1 on 2020-08-17 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_listings'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='description',
            field=models.TextField(default='No description'),
        ),
        migrations.AddField(
            model_name='listings',
            name='image',
            field=models.TextField(null=True),
        ),
    ]
