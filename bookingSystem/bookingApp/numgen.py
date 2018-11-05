# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 16:37:32 2018

@author: jvoyu
"""
from datetime import datetime
from django.utils import timezone
from random import randint as rnd


def generate():
    i = chr(75)
    j = chr(rnd(65, 68))
    k = chr(rnd(76, 84))
    l = str(rnd(100, 999))
    m = chr(rnd(85, 90))
    return (i + j + k + " " + l + m)


def createVehicle(a, b, c, d, e):
    for i in b.objects.all():
        for j in c.objects.all():
            for k in d.objects.all():
                for l in e.objects.all():
                    for h in range(24):
                        plate = generate()
                        if a.objects.filter(
                                numberPlate=plate).count() == 0 and (
                                h + 8) < 24 and j.location != k.location:
                            if h % 2 == 0 and i.vehicleMake.startswith(
                                    'Toyota'):
                                print(
                                    a.objects.create(
                                        numberPlate=plate,
                                        capacity=rnd(
                                            14,
                                            63),
                                        seatsTaken=rnd(
                                            0,
                                            9),
                                        destination=j,
                                        source=k,
                                        departureTime=datetime(
                                            2018,
                                            10,
                                            6,
                                            h,
                                            0),
                                        arrivalTime=datetime(
                                            2018,
                                            10,
                                            6,
                                            h + 8,
                                            0),
                                        saccoName=l,
                                        vehicleMake=i,
                                        seatType='business',
                                        seatPrice=2000,
                                        dateCreated=timezone.now()))
                            elif h % 2 != 0 and not i.vehicleMake.startswith('Toyota'):
                                print(
                                    a.objects.create(
                                        numberPlate=plate,
                                        capacity=rnd(
                                            14,
                                            63),
                                        seatsTaken=rnd(
                                            0,
                                            9),
                                        destination=j,
                                        source=k,
                                        departureTime=datetime(
                                            2018,
                                            10,
                                            6,
                                            h,
                                            0),
                                        arrivalTime=datetime(
                                            2018,
                                            10,
                                            6,
                                            h + 8,
                                            0),
                                        saccoName=l,
                                        vehicleMake=i,
                                        seatType='economy',
                                        seatPrice=1000,
                                        dateCreated=timezone.now()))
                        elif a.objects.filter(numberPlate=plate).count() == 0 and (h + 8) >= 24 and j.location != k.location:
                            if h % 2 == 0 and i.vehicleMake.startswith(
                                    'Toyota'):
                                print(
                                    a.objects.create(
                                        numberPlate=plate,
                                        capacity=rnd(
                                            14,
                                            63),
                                        seatsTaken=rnd(
                                            0,
                                            9),
                                        destination=j,
                                        source=k,
                                        departureTime=datetime(
                                            2018,
                                            10,
                                            6,
                                            h,
                                            0),
                                        arrivalTime=datetime(
                                            2018,
                                            10,
                                            6,
                                            ((h + 8) - 24),
                                            0),
                                        saccoName=l,
                                        vehicleMake=i,
                                        seatType='economy',
                                        seatPrice=1000,
                                        dateCreated=timezone.now()))
                            if h % 2 != 0 and not i.vehicleMake.startswith(
                                    'Toyota'):
                                print(
                                    a.objects.create(
                                        numberPlate=plate,
                                        capacity=rnd(
                                            14,
                                            63),
                                        seatsTaken=rnd(
                                            0,
                                            9),
                                        destination=j,
                                        source=k,
                                        departureTime=datetime(
                                            2018,
                                            10,
                                            6,
                                            h,
                                            0),
                                        arrivalTime=datetime(
                                            2018,
                                            10,
                                            6,
                                            ((h + 8) - 24),
                                            0),
                                        saccoName=l,
                                        vehicleMake=i,
                                        seatType='business',
                                        seatPrice=2000,
                                        dateCreated=timezone.now()))
                        h += 1
