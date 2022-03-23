# Generated by Django 3.2.12 on 2022-03-22 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_healthcareprofessional_schedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthcareprofessional',
            name='schedule',
            field=models.JSONField(default={}),
        ),
        migrations.AlterField(
            model_name='requests',
            name='distribution',
            field=models.JSONField(default={}),
        ),
        migrations.AlterField(
            model_name='requests',
            name='requirements',
            field=models.JSONField(default={}),
        ),
    ]