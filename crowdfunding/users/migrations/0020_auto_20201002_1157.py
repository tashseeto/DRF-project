# Generated by Django 3.0.8 on 2020-10-02 11:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_auto_20201002_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 2, 11, 57, 37, 556650, tzinfo=utc)),
        ),
    ]