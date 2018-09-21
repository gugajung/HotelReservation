# Generated by Django 2.0.4 on 2018-09-13 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotelReservation', '0041_auto_20180913_0033'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hotellist',
            options={'ordering': ('hotel_name',), 'verbose_name_plural': 'Hotels'},
        ),
        migrations.AlterField(
            model_name='reservation',
            name='room_type',
            field=models.CharField(default='', max_length=100),
        ),
    ]