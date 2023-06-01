from rest_framework import serializers
from .models import Location, Truck, Cargo

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'zip', 'lat', 'lng', 'city', 'state_name']


class TruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truck
        fields = ['id', 'number', 'zip', 'load_capacity']


class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = ['id', 'zip_pickup', 'zip_delivery', 'cargo', 'description', 'truck']
