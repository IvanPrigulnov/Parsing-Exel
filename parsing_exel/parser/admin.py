from django.contrib import admin
from .models import *


class BillboardsAdmin(admin.ModelAdmin):
    list_display = [
        'city', 'address', 'surface_type', 'lighting', 'product_restrictions',
        'permission',
              ]


class SidesAdmin(admin.ModelAdmin):
    list_display = [
        'internal_code', 'billboard', 'side', 'photo_or_scheme',
        'digital_views', 'media_material', 'note', 'date_update'
              ]


class ESPARAdmin(admin.ModelAdmin):
    list_display = [
        'ESPAR_code', 'GRP', 'OTS', 'billboard', 'side', 'date_update',
              ]


class SalesAdmin(admin.ModelAdmin):
    list_display = [
        'year', 'month', 'status', 'billboard', 'side', 'ESPAR', 'date_update'
              ]
    list_filter = ['year', 'month', 'status']


admin.site.register(Billboards, BillboardsAdmin)
admin.site.register(Sides, SidesAdmin)
admin.site.register(ESPAR, ESPARAdmin)
admin.site.register(Sales, SalesAdmin)




