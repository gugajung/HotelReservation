# Generated by Django 2.0.4 on 2018-09-01 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotelReservation', '0012_hotellist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotellist',
            name='description',
            field=models.TextField(default='', max_length=500),
        ),
    ]
