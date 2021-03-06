# Generated by Django 3.2.12 on 2022-03-21 01:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_requests_requirements'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requests',
            name='daysRequested',
        ),
        migrations.RemoveField(
            model_name='requests',
            name='endTime',
        ),
        migrations.RemoveField(
            model_name='requests',
            name='numDaysRequested',
        ),
        migrations.RemoveField(
            model_name='requests',
            name='startDate',
        ),
        migrations.RemoveField(
            model_name='requests',
            name='startTime',
        ),
        migrations.RemoveField(
            model_name='requests',
            name='takerID',
        ),
        migrations.AddField(
            model_name='requests',
            name='userID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.users'),
        ),
    ]
