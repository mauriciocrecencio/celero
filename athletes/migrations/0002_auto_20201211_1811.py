# Generated by Django 3.1.3 on 2020-12-11 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('athletes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='athlete_instance',
            old_name='athlete_id',
            new_name='athlete',
        ),
        migrations.RenameField(
            model_name='athlete_instance',
            old_name='event_id',
            new_name='event',
        ),
    ]
