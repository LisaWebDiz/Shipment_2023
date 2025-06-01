import django_filters
import pandas as pd
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django_filters import CharFilter
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .forms import LocationImportForm, CargoForm, TruckForm
from .models import Location, LocationImport, Truck, Cargo
from .serializer import LocationSerializer, TruckSerializer, CargoSerializer


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
            zip=l[0],
            lat=l[1],
            lng=l[2],
            city=l[3],
            state_name=l[5],
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
