# Generated by Django 3.1 on 2021-04-30 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_data_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='precipitation',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=100),
        ),
        migrations.AddField(
            model_name='data',
            name='windDirection',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='data',
            name='windSpeed',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=100),
        ),
        migrations.AlterField(
            model_name='data',
            name='pressure',
            field=models.DecimalField(decimal_places=2, max_digits=100),
        ),
        migrations.AlterField(
            model_name='data',
            name='temperature',
            field=models.DecimalField(decimal_places=2, max_digits=100),
        ),
    ]
