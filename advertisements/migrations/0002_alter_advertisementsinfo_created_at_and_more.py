# Generated by Django 4.0.4 on 2022-04-27 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisementsinfo',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='advertisementsinfo',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
    ]
