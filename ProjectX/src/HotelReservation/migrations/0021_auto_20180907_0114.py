# Generated by Django 2.0.4 on 2018-09-07 01:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HotelReservation', '0020_auto_20180907_0058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='user',
        ),
        migrations.DeleteModel(
            name='Reservation',
        ),
    ]
