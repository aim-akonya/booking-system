# Generated by Django 2.0 on 2018-11-03 15:18

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('location', models.CharField(max_length=128, primary_key=True, serialize=False, verbose_name='Location')),
            ],
        ),
        migrations.CreateModel(
            name='Hire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickUpDate', models.DateField(default=datetime.date.today, verbose_name='Pick up date')),
                ('returnDate', models.DateField(default=datetime.date.today, verbose_name='Return date')),
                ('number', models.PositiveSmallIntegerField(default=10, verbose_name='Total travellers')),
                ('hireTaken', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Make',
            fields=[
                ('vehicleMake', models.CharField(max_length=128, primary_key=True, serialize=False, verbose_name='Vehicle Make')),
            ],
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('location', models.CharField(max_length=128, primary_key=True, serialize=False, verbose_name='Location')),
            ],
        ),
        migrations.CreateModel(
            name='Parcel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Weight')),
                ('fragile', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=6, verbose_name='Fragile')),
                ('recipient', models.CharField(max_length=100, verbose_name='Recipient Name')),
                ('recipientId', models.CharField(default='12345678', max_length=8, verbose_name='Recipient ID')),
                ('datePlaced', models.DateTimeField(default=django.utils.timezone.now)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookingApp.Destination', verbose_name='To')),
            ],
        ),
        migrations.CreateModel(
            name='Sacco',
            fields=[
                ('username', models.CharField(max_length=128, verbose_name='Username')),
                ('saccoName', models.CharField(max_length=128, primary_key=True, serialize=False, verbose_name='Sacco Name')),
                ('num', models.PositiveSmallIntegerField(default=1, verbose_name='Number of vehicles')),
                ('hasBeenAdded', models.BooleanField(default=False)),
                ('location', models.ManyToManyField(to='bookingApp.Office', verbose_name='Areas of operation')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('numberPlate', models.CharField(default='Not available', max_length=128, primary_key=True, serialize=False, verbose_name='Number plate')),
                ('capacity', models.PositiveSmallIntegerField(verbose_name='Capacity')),
                ('seatsTaken', models.PositiveSmallIntegerField(default=10, verbose_name='Seats Taken')),
                ('departureTime', models.TimeField(default=django.utils.timezone.now, verbose_name='Depature')),
                ('arrivalTime', models.TimeField(default=django.utils.timezone.now, verbose_name='Arrival')),
                ('seatType', models.CharField(choices=[('economy', 'Economy'), ('business', 'Business')], max_length=20, verbose_name='Seat type')),
                ('seatPrice', models.SmallIntegerField(default=1000, verbose_name='Seat Price')),
                ('hirePrice', models.IntegerField(default=5000, verbose_name='Hire Price')),
                ('dateCreated', models.DateTimeField(default=django.utils.timezone.now)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookingApp.Destination', verbose_name='To')),
                ('saccoName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookingApp.Sacco', verbose_name='Sacco')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookingApp.Office', verbose_name='From')),
                ('vehicleMake', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookingApp.Make', verbose_name='Make')),
            ],
        ),
        migrations.AddField(
            model_name='parcel',
            name='saccoName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookingApp.Sacco', verbose_name='Sacco'),
        ),
        migrations.AddField(
            model_name='parcel',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookingApp.Office', verbose_name='From'),
        ),
        migrations.AddField(
            model_name='hire',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookingApp.Office', verbose_name='To'),
        ),
        migrations.AddField(
            model_name='hire',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookingApp.Destination', verbose_name='From'),
        ),
        migrations.AddField(
            model_name='hire',
            name='vehicleMake',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookingApp.Make', verbose_name='Vehicle Make'),
        ),
    ]
