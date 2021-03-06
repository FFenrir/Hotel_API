# Generated by Django 3.2.9 on 2022-05-11 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.IntegerField()),
                ('status', models.CharField(max_length=100)),
                ('lux', models.BooleanField()),
                ('booking_started', models.DateField(blank=True, null=True)),
                ('booking_ends', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
