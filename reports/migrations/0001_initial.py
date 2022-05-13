# Generated by Django 3.2.9 on 2022-05-11 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rooms', '0001_initial'),
        ('users', '0003_department_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_title', models.CharField(max_length=200)),
                ('report_description', models.TextField()),
                ('report_left_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Department_that_left_report', to='users.department')),
                ('report_left_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Department_that_report_is_left_to', to='users.department')),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='rooms.room')),
            ],
        ),
    ]