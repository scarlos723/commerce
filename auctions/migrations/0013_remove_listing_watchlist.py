# Generated by Django 3.1 on 2020-09-30 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_auto_20200919_0029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='watchlist',
        ),
    ]
