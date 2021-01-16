# Generated by Django 3.1 on 2020-08-17 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='listings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('bid', models.IntegerField(verbose_name=float)),
                ('category', models.CharField(max_length=64)),
            ],
        ),
    ]