# Generated by Django 2.0.4 on 2018-09-01 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotelReservation', '0017_auto_20180901_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotellist',
            name='image',
            field=models.FileField(blank=True, upload_to='media'),
        ),
    ]
