# Generated by Django 2.0.4 on 2018-09-14 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotelReservation', '0047_auto_20180914_0712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotellist',
            name='telephone',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
