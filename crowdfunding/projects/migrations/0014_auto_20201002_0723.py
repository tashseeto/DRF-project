# Generated by Django 3.0.8 on 2020-10-02 07:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_auto_20201002_0720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 2, 7, 23, 22, 652728, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='project',
            name='date_end',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 2, 7, 23, 22, 652764, tzinfo=utc)),
        ),
    ]
