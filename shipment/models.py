from django.db import models

import factory
import factory.django
from random import randint, sample, choice
import faker

from django.urls import reverse, reverse_lazy


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
    # zip_pickup = models.IntegerField()
    zip_pickup = models.ForeignKey(Location, on_delete=models.CASCADE)
    zip_delivery = models.IntegerField()
    cargo = models.FloatField()
    description = models.TextField()

    truck = models.ForeignKey(Truck, on_delete=models.CASCADE)

    def __str__(self):
        return self.id


# class Truck1(factory.django.DjangoModelFactory):
#     class Meta:
#         model = Truck
#
#     number = str(randint(1000, 9999)) + choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
#     zip = choice(Location.objects.values_list('zip', flat=True).distinct())
#     load_capacity = randint(1, 1000)
#
#
# class Truck2(Truck1):
#     number = str(randint(1000, 9999)) + choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
#     zip = choice(Location.objects.values_list('zip', flat=True).distinct())
#     load_capacity = randint(1, 1000)
#
# class Truck3(Truck1):
#     number = str(randint(1000, 9999)) + choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
#     zip = choice(Location.objects.values_list('zip', flat=True).distinct())
#     load_capacity = randint(1, 1000)
#
# class Truck4(Truck1):
#     number = str(randint(1000, 9999)) + choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
#     zip = choice(Location.objects.values_list('zip', flat=True).distinct())
#     load_capacity = randint(1, 1000)
#
# class Truck5(Truck1):
#     number = str(randint(1000, 9999)) + choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
#     zip = choice(Location.objects.values_list('zip', flat=True).distinct())
#     load_capacity = randint(1, 1000)
#
# class Truck6(Truck1):
#     number = str(randint(1000, 9999)) + choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
#     zip = choice(Location.objects.values_list('zip', flat=True).distinct())
#     load_capacity = randint(1, 1000)
#
# class Truck7(Truck1):
#     number = str(randint(1000, 9999)) + choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
#     zip = choice(Location.objects.values_list('zip', flat=True).distinct())
#     load_capacity = randint(1, 1000)
#
# class Truck8(Truck1):
#     number = str(randint(1000, 9999)) + choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
#     zip = choice(Location.objects.values_list('zip', flat=True).distinct())
#     load_capacity = randint(1, 1000)
#
# class Truck9(Truck1):
#     number = str(randint(1000, 9999)) + choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
#     zip = choice(Location.objects.values_list('zip', flat=True).distinct())
#     load_capacity = randint(1, 1000)
#
# class Truck10(Truck1):
#     number = str(randint(1000, 9999)) + choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
#     zip = choice(Location.objects.values_list('zip', flat=True).distinct())
#     load_capacity = randint(1, 1000)
#
# class Truck11(Truck1):
#     number = str(randint(1000, 9999)) + choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
#     zip = choice(Location.objects.values_list('zip', flat=True).distinct())
#     load_capacity = randint(1, 1000)
#
# class Truck12(Truck1):
#     number = str(randint(1000, 9999)) + choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
#     zip = choice(Location.objects.values_list('zip', flat=True).distinct())
#     load_capacity = randint(1, 1000)
#
# class Truck13(Truck1):
#     number = str(randint(1000, 9999)) + choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
#     zip = choice(Location.objects.values_list('zip', flat=True).distinct())
#     load_capacity = randint(1, 1000)
#
# class Truck14(Truck1):
#     number = str(randint(1000, 9999)) + choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
#     zip = choice(Location.objects.values_list('zip', flat=True).distinct())
#     load_capacity = randint(1, 1000)
#
# class Truck15(Truck1):
#     number = str(randint(1000, 9999)) + choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
#     zip = choice(Location.objects.values_list('zip', flat=True).distinct())
#     load_capacity = randint(1, 1000)
#
# class Truck16(Truck1):
#     number = str(randint(1000, 9999)) + choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
#     zip = choice(Location.objects.values_list('zip', flat=True).distinct())
#     load_capacity = randint(1, 1000)
#
# class Truck17(Truck1):
#     number = str(randint(1000, 9999)) + choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
#     zip = choice(Location.objects.values_list('zip', flat=True).distinct())
#     load_capacity = randint(1, 1000)
#
# class Truck18(Truck1):
#     number = str(randint(1000, 9999)) + choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
#     zip = choice(Location.objects.values_list('zip', flat=True).distinct())
#     load_capacity = randint(1, 1000)
#
# class Truck19(Truck1):
#     number = str(randint(1000, 9999)) + choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
#     zip = choice(Location.objects.values_list('zip', flat=True).distinct())
#     load_capacity = randint(1, 1000)
#
# class Truck20(Truck1):
#     number = str(randint(1000, 9999)) + choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
#     zip = choice(Location.objects.values_list('zip', flat=True).distinct())
#     load_capacity = randint(1, 1000)








