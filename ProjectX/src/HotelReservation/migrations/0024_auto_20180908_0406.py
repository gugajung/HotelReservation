# Generated by Django 2.0.4 on 2018-09-08 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotelReservation', '0023_auto_20180907_1744'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotellist',
            name='room_type',
        ),
        migrations.AddField(
            model_name='reservation',
            name='first_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='reservation',
            name='last_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='reservation',
            name='room_type',
            field=models.CharField(choices=[('Single_Bed', 'Single'), ('Double_bed', 'Double')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='reservation',
            name='total_days',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='date_in',
            field=models.DateField(),
        ),
    ]
