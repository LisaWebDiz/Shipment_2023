from random import randint, choice

from django.db import models


class Location(models.Model):
    zip = models.IntegerField()
    lat = models.CharField(max_length=20)
    lng = models.CharField(max_length=20)
    city = models.CharField(max_length=30)
    state_name = models.CharField(max_length=30)

    class Meta:
        ordering = ['zip']


class LocationImport(models.Model):
    file = models.FileField(upload_to='uploads/')
    date_added = models.DateTimeField(auto_now_add=True)


class Truck(models.Model):
    number = models.CharField(max_length=5)
    zip = models.IntegerField()
    load_capacity = models.IntegerField()


def data():
    number = str(randint(1000, 9999)) + choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    return number


class Cargo(models.Model):
    zip_pickup = models.ForeignKey(Location, on_delete=models.CASCADE)
    zip_delivery = models.IntegerField()
    cargo = models.FloatField()
    description = models.TextField()

    truck = models.ForeignKey(Truck, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
