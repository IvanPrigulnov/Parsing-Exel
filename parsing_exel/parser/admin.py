from django.contrib import admin

from import_export.admin import ImportExportModelAdmin
from import_export import resources
from import_export.fields import Field
from .models import *


class BillboardsResources(resources.ModelResource):
    id = Field(attribute='id', column_name='ID Билборда')
    city = Field(attribute='city', column_name='Города')
    surface_type = Field(attribute='surface_type', column_name='Тип поверхности')
    lighting = Field(attribute='lighting', column_name='Освещение')
    address = Field(attribute='address', column_name='Адрес')
    latitude = Field(attribute='latitude', column_name='Широта')
    longitude = Field(attribute='longitude', column_name='Долгота')
    product_restrictions = Field(attribute='product_restrictions', column_name='Ограничения по продукту')
    district = Field(attribute='district', column_name='Городской округ')
    permission = Field(attribute='permission', column_name='Разрешение ПО')

    class Meta:
        model = Billboards
        exclude = ('date_create', 'date_update')


class BillboardsAdmin(ImportExportModelAdmin):
    list_display = [field.name for field in Billboards._meta.fields if field.name != 'id']
    resource_classes = [BillboardsResources]


admin.site.register(Billboards, BillboardsAdmin)


class SidesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Sides._meta.fields if field.name != 'id']


class ESPARAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ESPAR._meta.fields if field.name != 'id']


class SalesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Sales._meta.fields if field.name != 'id']
    list_filter = ['year', 'month', 'status']



admin.site.register(Sides, SidesAdmin)
admin.site.register(ESPAR, ESPARAdmin)
admin.site.register(Sales, SalesAdmin)




