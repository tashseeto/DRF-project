# Generated by Django 3.0.8 on 2020-10-02 06:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20201002_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 2, 6, 55, 6, 329724, tzinfo=utc)),
        ),
    ]
