from django.shortcuts import render, get_object_or_404, redirect
from .models import Location, LocationImport, Truck, Cargo#, Truck1, Truck2, Truck3, Truck4, Truck5, Truck6, Truck7, Truck8, Truck9, Truck10, Truck11, Truck12, Truck13, Truck14, Truck15, Truck16, Truck17, Truck18,Truck19,Truck20
from .forms import LocationImportForm, CargoForm, TruckForm
import pandas as pd
from django.core.management import call_command

from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from django.utils.decorators import method_decorator

from django.http import JsonResponse
from .serializer import LocationSerializer, TruckSerializer, CargoSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets

import django_filters
from django_filters import CharFilter

from geopy import distance

from django.core.paginator import Paginator



def index(request):
    return render(request, 'shipment_html/index.html')


class CargoSearch(django_filters.FilterSet):
    id = CharFilter(field_name='id')

    class Meta:
        model = Cargo
        fields = ['id']


def search_cargo(request):
    cargos = CargoSearch(request.GET, queryset=Cargo.objects.all()).qs
    context = {
        'cargos': cargos,
    }
    return render(request, 'shipment_html/cargo_search.html', context)


def create_db(file_path):
    df = pd.read_csv(file_path, delimiter=',')
    list_of_csv = [list(row) for row in df.values]

    for l in list_of_csv:
        Location.objects.create(
            zip = l[0],
            lat = l[1],
            lng = l[2],
            city = l[3],
            state_name = l[5],
        )


def upload_locations(request):
    if request.method == 'POST':
        form = LocationImportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            file = request.FILES["file"]
            obj = LocationImport.objects.create(file=file)
            create_db(obj.file)
            return redirect('index')
    else:
        form = LocationImportForm()
        return render(request, 'shipment_html/upload_form.html', {'form': form})


def upload_trucks(request):
    call_command('loaddata', 'shipment/fixtures/trucks.json')
    # Truck1.create()
    # Truck2.create()
    # Truck3.create()
    # Truck4.create()
    # Truck5.create()
    # Truck6.create()
    # Truck7.create()
    # Truck8.create()
    # Truck9.create()
    # Truck10.create()
    # Truck11.create()
    # Truck12.create()
    # Truck13.create()
    # Truck14.create()
    # Truck15.create()
    # Truck16.create()
    # Truck17.create()
    # Truck18.create()
    # Truck19.create()
    # Truck20.create()
    return redirect('index')


@api_view(['GET', 'POST'])
def shipment_locations_api_list(request):
    if request.method == 'GET':
        locations_list = Location.objects.all()
        serializer = LocationSerializer(locations_list, many=True)
        # return JsonResponse({'locations_list': serializer.data})
        return Response({'locations_list': serializer.data})
    elif request.method == 'POST':
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def shipment_location_api_detail(request, pk, format=None):
        location_obj = get_object_or_404(Location, pk=pk)
        if location_obj:
            if request.method == 'GET':
                serializer = LocationSerializer(location_obj)
                return Response(serializer.data)
            elif request.method == 'PUT':
                serializer = LocationSerializer(location_obj, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'message': "Данные успешно изменены", 'shipment': serializer.data})
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            elif request.method == 'DELETE':
                location_obj.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
def shipment_trucks_api_list(request):
    if request.method == 'GET':
        trucks_list = Truck.objects.all()
        serializer = TruckSerializer(trucks_list, many=True)
        # return JsonResponse({'trucks_list': serializer.data})
        return Response({'trucks_list': serializer.data})
    elif request.method == 'POST':
        serializer = TruckSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def shipment_truck_api_detail(request, pk, format=None):
        truck_obj = get_object_or_404(Truck, pk=pk)
        if truck_obj:
            if request.method == 'GET':
                serializer = TruckSerializer(truck_obj)
                return Response(serializer.data)
            elif request.method == 'PUT':
                serializer = TruckSerializer(truck_obj, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'message': "Данные успешно изменены", 'shipment': serializer.data})
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            elif request.method == 'DELETE':
                truck_obj.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
def shipment_cargos_api_list(request):
    if request.method == 'GET':
        cargos_list = Cargo.objects.all()
        serializer = CargoSerializer(cargos_list, many=True)
        # return JsonResponse({'cargos_list': serializer.data})
        return Response({'cargos_list': serializer.data})
    elif request.method == 'POST':
        serializer = CargoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def shipment_cargo_api_detail(request, pk, format=None):
        cargo_obj = get_object_or_404(Cargo, pk=pk)
        if cargo_obj:
            if request.method == 'GET':
                serializer = CargoSerializer(cargo_obj)
                return Response(serializer.data)
            elif request.method == 'PUT':
                serializer = CargoSerializer(cargo_obj, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'message': "Данные успешно изменены", 'shipment': serializer.data})
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            elif request.method == 'DELETE':
                cargo_obj.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


def cargos(request):
    cargos_list = Cargo.objects.all()

    context = {
        'cargos_list': cargos_list,
    }

    paginator = Paginator(Cargo.objects.all(), 10)
    page_num = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_num)
    context['page_obj'] = page_objects
    return render(request, 'shipment_html/cargos_list.html', context)


class CargoCreateView(CreateView):
    model = Cargo
    form_class = CargoForm
    template_name = 'shipment_html/add_cargo.html'
    context_object_name = 'form'
    success_url = reverse_lazy('shipment_cargos_api_list')


    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class CargoUpdateView(UpdateView):
    model = Cargo
    form_class = CargoForm
    template_name = 'shipment_html/cargo_edit.html'
    context_object_name = 'form'
    success_url = reverse_lazy('shipment_cargos_api_list')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class CargoDeleteView(DeleteView):
    model = Cargo
    success_url = reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


def trucks(request):
    trucks_list = Truck.objects.all()

    context = {
        'trucks_list': trucks_list,
    }

    paginator = Paginator(Truck.objects.all(), 10)
    page_num = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_num)
    context['page_obj'] = page_objects
    return render(request, 'shipment_html/trucks_list.html', context)


class TruckUpdateView(UpdateView):
    model = Truck
    form_class = TruckForm
    template_name = 'shipment_html/truck_edit.html'
    context_object_name = 'form'
    success_url = reverse_lazy('shipment_trucks_api_list')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)




#
# def main(request):
#     zip = list(Location.objects.all().values_list('zip', 'lat', 'lng', named=True))
#     cargo_zip = list(Cargo.objects.all().values_list('zip_pickup', flat=True))
#     truck_zip = list(Truck.objects.all().values_list('zip', flat=True))
#     if cargo_zip[0] == zip[0]:
#         point_1 = (zip[1], zip[2])
#         if truck_zip[0] == zip[0]:
#             point_2 = (zip[1], zip[2])
#             distance = point_2
#     #         distance = distance.distance(point_1, point_2).miles
#     # if distance <= 450:
#     #     return truck_zip
#
#     context = {
#         'distance': distance,
#         'cargo_zip': cargo_zip,
#         'zip': zip,
#         'truck_zip': truck_zip,
#
#     }
#     return render(request, 'shipment_html/main.html', context)
#
# # def search_cargo(request):
#     # myFilter = CargoSearch(request.GET, queryset=Cargo.objects.all())
#     # cargos = myFilter.qs
#     # myFilter2 = ZipSearch(request.GET, queryset=Location.objects.all())
#     # zips = myFilter2.qs
#     # zips = Location.objects.all()
#     # cargos = CargoSearch(request.GET, queryset=Cargo.objects.all()).qs
#     # cargos_list = list(cargos)
#     # zips = ZipSearch(request.GET, queryset=Cargo.objects.all()).qs
#
#     # zip_cargo = Cargo.objects.filter('zip_pickup')
#     # location_zip = Location.objects.filter('zip')
#     # lat = Location.objects.filter('lat')
#     # lng = Location.objects.filter('lng')
#     # # cargo = Cargo.objects.filter('zip_pickup')
#     # location_truck = Truck.objects.filter('zip')
#     # for i in location_zip:
#     #     if cargos_list[1] == i:
#     #         point_1 = (lat, lng)
#     # for l in location_truck:
#     #     if cargos_list[1] == l:
#     #         point_2 = (lat, lng)
#     # distance = distance.distance(point_1, point_2).miles
#
#
#
#     # context = {
#     #     'cargos': cargos,
#         # 'zip_cargo': zip_cargo,
#         # 'location_zip': location_zip,
#         # 'lat': lat,
#         # 'lng': lng,
#         # 'location_truck': location_truck,
#         # 'distance': distance
#
#
#     # }
#     # return render(request, 'shipment_html/cargo_search.html', context)
