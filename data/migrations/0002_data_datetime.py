# Generated by Django 3.1 on 2021-04-30 11:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='dateTime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
