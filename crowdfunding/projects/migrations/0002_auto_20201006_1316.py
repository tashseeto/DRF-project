# Generated by Django 3.0.8 on 2020-10-06 13:16

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='date_end',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 6, 13, 16, 7, 333268, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='project',
            name='num_suppoters',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='project',
            name='total_raised',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='project',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 6, 13, 16, 7, 333238, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='project',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner_projects', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Pledge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('comment', models.CharField(max_length=200)),
                ('anonymous', models.BooleanField()),
                ('date_created', models.DateTimeField(default=datetime.datetime(2020, 10, 6, 13, 16, 7, 344306, tzinfo=utc))),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pledges', to='projects.Project')),
                ('supporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supporter_pledges', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]