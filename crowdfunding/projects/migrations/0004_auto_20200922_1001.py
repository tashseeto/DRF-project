# Generated by Django 3.0.8 on 2020-09-22 10:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20200911_2341'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='date_end',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 22, 10, 1, 27, 5579, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='project',
            name='total_raised',
            field=models.IntegerField(default=0),
        ),
    ]
