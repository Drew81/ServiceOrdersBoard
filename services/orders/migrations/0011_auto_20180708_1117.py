# Generated by Django 2.0.6 on 2018-07-08 11:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_auto_20180708_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='updated',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 7, 8, 11, 17, 51, 477026, tzinfo=utc)),
        ),
    ]
