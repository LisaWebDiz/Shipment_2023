from django.contrib import admin
from .models import Location, LocationImport, Truck, Cargo

from import_export.admin import ImportExportModelAdmin
from import_export import resources
from import_export import fields

import csv
from .forms import LocationImportForm
from django.urls import path
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages



class LocationResource(resources.ModelResource):

    class Meta:
        model = Location
        import_id_fields = ('zip', 'lat', 'lng', 'city', 'state_name',)


class LocationAdmin(ImportExportModelAdmin):
    resource_classes = [LocationResource]
    list_display = ('zip', 'lat', 'lng', 'city', 'state_name',)
    # list_display_links = ('id', 'zip')
    # search_fields = ('id', 'zip', 'city', 'state_name')
    # # list_editable = ()
    # # list_filter = ()

admin.site.register(Location, LocationAdmin)

class TruckAdmin(admin.ModelAdmin):
    list_display = ('number', 'zip', 'load_capacity',)

admin.site.register(Truck, TruckAdmin)


class CargoAdmin(admin.ModelAdmin):
    list_display = ('zip_pickup', 'zip_delivery', 'cargo', 'description', 'truck',)

admin.site.register(Cargo, CargoAdmin)







# @admin.register(LocationImport)
# class LocationImportAdmin(admin.ModelAdmin):
#     list_display = ('csv_file', 'date_added')
#
#



# @admin.register(Location)
# class LocationAdmin(admin.ModelAdmin):
#     list_display = ('id', 'zip', 'lat', 'lng', 'city', 'state_name')
#     list_display_links = ('id', 'zip')
#     search_fields = ('id', 'zip', 'city', 'state_name')
#     # list_editable = ()
#     # list_filter = ()
#
#     def get_urls(self):
#         urls = super().get_urls()
#         urls.insert(-1, path('csv-upload/', self.upload_csv))
#         return urls
#
#     def upload_csv(self, request):
#         if request.method == 'POST':
#             form = LocationImportForm(request.POST, request.FILES)
#             if form.is_valid():
#                 # сохраняем загруженный файл и делаем запись в базу
#                 form_object = form.save()
#                 # обработка csv файла
#                 with form_object.csv_file.open('r') as csv_file:
#                     rows = csv.reader(csv_file, delimiter=',')
#                     # if next(rows) != ['name', 'author', 'publish_date']:
#                     #     # обновляем страницу пользователя
#                     #     # с информацией о какой-то ошибке
#                     #     messages.warning(request, 'Неверные заголовки у файла')
#                     #     return HttpResponseRedirect(request.path_info)
#                     for row in rows:
#                         # print(row[2])
#                         # добавляем данные в базу
#                         Location.objects.update_or_create(
#                             zip=row[0],
#                             lat=row[1],
#                             lng=row[2],
#                             city=row[3]
#                         )
#                 # конец обработки файлы
#                 # перенаправляем пользователя на главную страницу
#                 # с сообщением об успехе
#                 url = reverse('admin:index')
#                 messages.success(request, 'Файл успешно импортирован')
#                 return HttpResponseRedirect(url)
#         form = LocationImportForm()
#         return render(request, 'admin/main.html', {'form': form})

# admin.site.register(Location, LocationAdmin, LocationImportAdmin)





















