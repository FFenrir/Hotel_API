# Generated by Django 3.2.9 on 2022-05-07 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20220506_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='phone_number',
            field=models.IntegerField(null=True),
        ),
    ]
