# Generated by Django 3.2.12 on 2022-04-12 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0053_alter_requests_end'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerequest',
            name='status',
            field=models.CharField(max_length=100),
        ),
    ]