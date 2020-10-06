# Generated by Django 3.0.8 on 2020-10-06 11:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20201006_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pledge',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2020, 10, 6, 11, 49, 55, 902011, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='project',
            name='num_supporters',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='project',
            name='total_raised',
            field=models.IntegerField(default=0),
        ),
    ]
