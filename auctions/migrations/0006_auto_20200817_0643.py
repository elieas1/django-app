# Generated by Django 3.1 on 2020-08-17 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auto_20200817_0641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='image',
            field=models.TextField(blank=True, null=True),
        ),
    ]
