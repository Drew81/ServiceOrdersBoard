# Generated by Django 2.0.6 on 2018-06-29 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]
