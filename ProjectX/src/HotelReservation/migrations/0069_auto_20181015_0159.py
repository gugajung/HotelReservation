# Generated by Django 2.0.4 on 2018-10-15 01:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HotelReservation', '0068_cardnumber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cardnumber',
            name='user',
        ),
        migrations.DeleteModel(
            name='CardNumber',
        ),
    ]
