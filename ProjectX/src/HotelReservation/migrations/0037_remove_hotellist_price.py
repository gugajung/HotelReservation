# Generated by Django 2.0.4 on 2018-09-11 02:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HotelReservation', '0036_remove_room_view'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotellist',
            name='price',
        ),
    ]