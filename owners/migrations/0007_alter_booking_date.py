# Generated by Django 4.0 on 2022-04-03 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owners', '0006_alter_booking_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.CharField(max_length=20),
        ),
    ]
