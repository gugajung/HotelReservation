# Generated by Django 2.0.4 on 2018-09-08 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotelReservation', '0025_auto_20180908_0426'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hotellist',
            options={'verbose_name_plural': 'Hotels'},
        ),
        migrations.AlterField(
            model_name='reservation',
            name='date_in',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='date_out',
            field=models.DateField(auto_now=True),
        ),
    ]