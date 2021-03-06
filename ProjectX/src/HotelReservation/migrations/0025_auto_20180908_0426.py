# Generated by Django 2.0.4 on 2018-09-08 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotelReservation', '0024_auto_20180908_0406'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hotellist',
            options={'verbose_name_plural': 'Hotel'},
        ),
        migrations.AddField(
            model_name='hotellist',
            name='Address',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='hotellist',
            name='City',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='hotellist',
            name='Country',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='hotellist',
            name='Telephone',
            field=models.CharField(default='', max_length=255),
        ),
    ]
