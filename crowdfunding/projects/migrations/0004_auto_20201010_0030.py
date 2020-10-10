# Generated by Django 3.0.8 on 2020-10-10 00:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20201006_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pledge',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='project',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='project',
            name='date_end',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]