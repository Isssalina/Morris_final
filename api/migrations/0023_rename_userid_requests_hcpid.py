# Generated by Django 3.2.12 on 2022-03-17 04:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_rename_publisher_requests_takerid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requests',
            old_name='userID',
            new_name='hcpID',
        ),
    ]
