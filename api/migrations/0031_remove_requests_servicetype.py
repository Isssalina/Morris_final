# Generated by Django 3.2.12 on 2022-03-25 04:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0030_healthcareprofessional_dateofbirth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requests',
            name='serviceType',
        ),
    ]