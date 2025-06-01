from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Location, Truck, Cargo


class LocationResource(resources.ModelResource):

    class Meta:
        model = Location
        import_id_fields = ('zip', 'lat', 'lng', 'city', 'state_name',)


class LocationAdmin(ImportExportModelAdmin):
    resource_classes = [LocationResource]
    list_display = ('zip', 'lat', 'lng', 'city', 'state_name',)


admin.site.register(Location, LocationAdmin)


class TruckAdmin(admin.ModelAdmin):
    list_display = ('number', 'zip', 'load_capacity',)


admin.site.register(Truck, TruckAdmin)


class CargoAdmin(admin.ModelAdmin):
    list_display = ('zip_pickup', 'zip_delivery', 'cargo', 'description', 'truck',)


admin.site.register(Cargo, CargoAdmin)
