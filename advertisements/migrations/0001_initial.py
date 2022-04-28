# Generated by Django 4.0.4 on 2022-04-28 00:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('advertisers', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advertisement_uid', models.CharField(max_length=65, unique=True)),
                ('advertiser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advertisers.advertiser')),
            ],
        ),
        migrations.CreateModel(
            name='AdvertisementInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.PositiveIntegerField(default=0)),
                ('impression', models.PositiveIntegerField(default=0)),
                ('click', models.PositiveIntegerField(default=0)),
                ('conversion', models.PositiveIntegerField(default=0)),
                ('cv', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('media', models.CharField(choices=[('naver', 'Naver'), ('kakao', 'Kakao'), ('google', 'Google'), ('facebook', 'Facebook')], max_length=15)),
                ('advertisement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advertisements.advertisement')),
            ],
        ),
    ]
