# Generated by Django 3.2.12 on 2022-03-25 03:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0029_remove_requests_hcpid'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthcareprofessional',
            name='dateOfBirth',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
