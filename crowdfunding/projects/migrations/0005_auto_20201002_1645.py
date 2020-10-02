# Generated by Django 3.0.8 on 2020-10-02 06:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20200922_1001'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='num_supporters',
            field=models.IntegerField(default=datetime.datetime(2020, 10, 2, 6, 45, 20, 393368, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='project',
            name='date_end',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='total_raised',
            field=models.IntegerField(),
        ),
    ]
