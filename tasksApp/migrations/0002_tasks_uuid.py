# Generated by Django 4.0.4 on 2022-05-11 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasksApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='uuid',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
