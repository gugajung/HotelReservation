# Generated by Django 2.0.4 on 2018-11-26 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HotelReservation', '0083_reservation_switch1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='switch1',
        ),
    ]
