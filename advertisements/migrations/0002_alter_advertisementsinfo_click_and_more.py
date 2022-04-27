# Generated by Django 4.0.4 on 2022-04-27 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisementsinfo',
            name='click',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='advertisementsinfo',
            name='conversion',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='advertisementsinfo',
            name='cost',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='advertisementsinfo',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='advertisementsinfo',
            name='cv',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='advertisementsinfo',
            name='impression',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='advertisementsinfo',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
