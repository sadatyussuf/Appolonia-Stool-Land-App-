# from django.contrib import admin
# from django.contrib.gis.db import models
from django.contrib.gis.admin import OSMGeoAdmin

from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Plot


@admin.register(Plot)
class PlotAdmin(LeafletGeoAdmin):
    list_display = ('owner_name', 'address','hometown','zone','phone_number','file_upload',)

class PlotAdmin(admin.ModelAdmin):
    pass
    
