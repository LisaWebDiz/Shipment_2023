from django.urls import path

from shipment.views import *

urlpatterns = [
    path('', index, name="index"),

    path('upload-locations', upload_locations, name='upload_locations'),
    path('cargo/search/', search_cargo, name='search_cargo'),

    path('api/locations/list', shipment_locations_api_list, name='shipment_locations_api_list'),
    path('api/locations/detail/<int:pk>', shipment_location_api_detail, name='shipment_location_api_detail'),

    path('trucks/', trucks, name='trucks_list'),
    path('api/trucks/list', shipment_trucks_api_list, name='shipment_trucks_api_list'),
    path('api/truck/detail/<int:pk>', shipment_truck_api_detail, name='shipment_truck_api_detail'),
    path('truck/update/<int:pk>/', TruckUpdateView.as_view(), name='edit_truck'),

    path('cargos/', cargos, name='cargos_list'),
    path('api/cargos/list', shipment_cargos_api_list, name='shipment_cargos_api_list'),
    path('api/cargo/detail/<int:pk>', shipment_cargo_api_detail, name='shipment_cargo_api_detail'),
    path('cargo/add/', CargoCreateView.as_view(), name='add_cargo'),
    path('cargo/update/<int:pk>/', CargoUpdateView.as_view(), name='edit_cargo'),
    path('cargo/del/<int:pk>/', CargoDeleteView.as_view(), name='del_cargo'),

]
