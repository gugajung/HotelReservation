# Generated by Django 2.0.4 on 2018-09-12 23:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HotelReservation', '0038_auto_20180911_0455'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotellist',
            name='Address',
        ),
        migrations.RemoveField(
            model_name='hotellist',
            name='City',
        ),
        migrations.RemoveField(
            model_name='hotellist',
            name='Country',
        ),
        migrations.RemoveField(
            model_name='hotellist',
            name='Telephone',
        ),
        migrations.RemoveField(
            model_name='hotellist',
            name='description',
        ),
        migrations.RemoveField(
            model_name='hotellist',
            name='image',
        ),
        migrations.RemoveField(
            model_name='hotellist',
            name='max_number_of_guests',
        ),
        migrations.RemoveField(
            model_name='room',
            name='Capacity',
        ),
        migrations.RemoveField(
            model_name='room',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='room',
            name='price',
        ),
    ]
