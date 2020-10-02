# Generated by Django 3.0.8 on 2020-10-02 11:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0018_auto_20201002_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 2, 11, 53, 59, 566865, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='project',
            name='num_supporters',
            field=models.IntegerField(default=0),
        ),
    ]
