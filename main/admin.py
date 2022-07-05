from django.contrib import admin
from django.contrib.gis.db import models
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Plot


@admin.register(Plot)
class PlotAdmin(OSMGeoAdmin):
    list_display = ('owner_name', 'zone', 'phone_number')

class PlotAdmin(admin.ModelAdmin):
    pass
    
