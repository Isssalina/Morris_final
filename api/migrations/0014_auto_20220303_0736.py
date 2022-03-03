# Generated by Django 3.2.12 on 2022-03-03 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_advertise_assigned'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advertise',
            old_name='assigned',
            new_name='deleted',
        ),
        migrations.AddField(
            model_name='caretaker',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='healthcareprofessional',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='requests',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='roles',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='securityquestions',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='users',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]