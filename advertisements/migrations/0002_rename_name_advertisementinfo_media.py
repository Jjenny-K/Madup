# Generated by Django 4.0.4 on 2022-04-28 01:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advertisementinfo',
            old_name='name',
            new_name='media',
        ),
    ]
