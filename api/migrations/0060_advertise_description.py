# Generated by Django 3.2.12 on 2022-04-15 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0059_auto_20220415_0426'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertise',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
