# Generated by Django 4.0 on 2022-04-02 07:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owners', '0004_remove_booking_slote_id_alter_booking_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slote',
            name='slote',
        ),
        migrations.AddField(
            model_name='booking',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='booking',
            name='time',
            field=models.CharField(default='NULL', max_length=20),
        ),
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(default='availabe', max_length=10),
        ),
    ]