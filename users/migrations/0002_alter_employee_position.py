# Generated by Django 3.2.9 on 2022-05-06 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.CharField(max_length=70, null=True),
        ),
    ]
