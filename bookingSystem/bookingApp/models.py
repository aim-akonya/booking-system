from django.db import models
from django.utils import timezone
import datetime
# Create your models here.


class Destination(models.Model):
    location = models.CharField(
        max_length=128,
        primary_key=True,
        default="Kisumu",
        verbose_name="Location")

    def addLocation(self):
        Destination.save(self)

    def __str__(self):
        return self.location


class Office(models.Model):
    location = models.CharField(
        max_length=128,
        primary_key=True,
        default="Kisumu",
        verbose_name="Location")

    def addLocation(self):
        Office.save(self)

    def __str__(self):
        return self.location


class Make(models.Model):
    vehicleMake = models.CharField(
        max_length=128,
        primary_key=True,
        default="Add",
        verbose_name="Vehicle Make")

    def addVehicle(self):
        Make.save(self)

    def __str__(self):
        return self.vehicleMake


class Hire(models.Model):
    location = models.ForeignKey(
        Destination,
        on_delete=models.CASCADE,
        verbose_name="From")
    destination = models.ForeignKey(
        Office, on_delete=models.CASCADE, verbose_name="To")
    pickUpDate = models.DateField(
        default=datetime.date.today,
        verbose_name="Pick up date")
    returnDate = models.DateField(
        default=datetime.date.today,
        verbose_name="Return date")
    number = models.PositiveSmallIntegerField(
        default=10, verbose_name="Total travellers")
    vehicleMake = models.ForeignKey(
        Make,
        on_delete=models.CASCADE,
        verbose_name="Vehicle Make")
    hireTaken = models.BooleanField(default=False)


class Sacco(models.Model):
    username = models.CharField(max_length=128, verbose_name='Username')
    saccoName = models.CharField(
        max_length=128,
        primary_key=True,
        default="Add sacco name",
        verbose_name='Sacco Name')
    num = models.PositiveSmallIntegerField(
        default=1, verbose_name="Number of vehicles")
    location = models.ManyToManyField(
        Office, verbose_name="Areas of operation")
    hasBeenAdded = models.BooleanField(default=False)

    def __str__(self):
        return self.saccoName


class Vehicle(models.Model):
    numberPlate = models.CharField(
        max_length=128,
        primary_key=True,
        default='Not available',
        verbose_name="Number plate")
    capacity = models.PositiveSmallIntegerField(default=14,verbose_name="Capacity")
    seatsTaken = models.PositiveSmallIntegerField(
        default=10, verbose_name="Seats Taken")
    destination = models.ForeignKey(
        Destination,
        on_delete=models.CASCADE,
        verbose_name="To")
    source = models.ForeignKey(
        Office,
        on_delete=models.CASCADE,
        verbose_name="From")
    departureTime = models.TimeField(
        default=timezone.now,
        verbose_name="Depature")
    arrivalTime = models.TimeField(
        default=timezone.now,
        verbose_name="Arrival")
    saccoName = models.ForeignKey(
        Sacco,
        on_delete=models.CASCADE,
        verbose_name="Sacco")
    vehicleMake = models.ForeignKey(
        Make, on_delete=models.CASCADE, verbose_name="Make")
    seatType = models.CharField(
        choices=(
            ('economy',
             'Economy'),
            ('business',
             'Business')),
        max_length=20,
        verbose_name="Seat type")
    seatPrice = models.SmallIntegerField(
        default=1000, verbose_name="Seat Price")
    hirePrice = models.IntegerField(default=5000, verbose_name="Hire Price")
    dateCreated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.numberPlate


class Parcel(models.Model):
    weight = models.DecimalField(
        default=0.0,
        max_digits=4,
        decimal_places=2,
        verbose_name="Weight")
    fragile = models.CharField(
        choices=(('Y', 'Yes'), ('N', 'No')), max_length=6, verbose_name="Fragile")
    destination = models.ForeignKey(
        Destination,
        on_delete=models.CASCADE,
        verbose_name="To")
    source = models.ForeignKey(
        Office,
        on_delete=models.CASCADE,
        verbose_name="From")
    recipient = models.CharField(max_length=100, verbose_name="Recipient Name")
    recipientId = models.CharField(
        default='12345678',
        max_length=8,
        verbose_name="Recipient ID")
    saccoName = models.ForeignKey(
        Sacco,
        on_delete=models.CASCADE,
        verbose_name="Sacco")
    datePlaced = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.recipientId)
