# Generated by Django 3.2.12 on 2022-03-16 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20220316_0622'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthcareprofessional',
            name='salary',
            field=models.FloatField(default=0),
        ),
    ]
