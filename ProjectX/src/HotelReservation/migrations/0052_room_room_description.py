# Generated by Django 2.0.4 on 2018-09-15 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotelReservation', '0051_hotellist_telephone'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='room_description',
            field=models.CharField(default='', max_length=255),
        ),
    ]