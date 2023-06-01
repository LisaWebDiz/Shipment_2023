from django.forms import ModelForm
from django import forms
from .models import LocationImport, Cargo, Truck


class LocationImportForm(ModelForm):
    class Meta:
        model = LocationImport
        fields = ('file',)


class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        # fields = '__all__'
        fields = ['zip_pickup', 'zip_delivery', 'cargo', 'description', 'truck']

        widgets = {
            'zip_pickup': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'floatingInput',
                    'placeholder': "Забрать из"
                }
            ),
            'zip_delivery': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Доставить до"
                }
            ),
            'cargo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Вес"
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Описание"
                }
            ),
            'truck': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Грузовик"
                }
            ),
        }


class TruckForm(forms.ModelForm):
    class Meta:
        model = Truck
        # fields = '__all__'
        fields = ['number', 'zip', 'load_capacity', ]

        widgets = {
            'number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'floatingInput',
                    'placeholder': "Номер грузовика",
                }
            ),
            'zip': forms.TextInput(
                attrs = {
            'class': 'form-control',
            'placeholder': "zip"
        }
        ),
        'load_capacity': forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Грузоподъемность"
            }
        ),
        }
