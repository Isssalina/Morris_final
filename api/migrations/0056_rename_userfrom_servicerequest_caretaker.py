# Generated by Django 3.2.12 on 2022-04-15 03:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0055_remove_servicerequest_userto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicerequest',
            old_name='userFrom',
            new_name='caretaker',
        ),
    ]