from django.contrib import admin
from django.contrib.gis.db import models
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(OSMGeoAdmin):
    list_display = ('first_name', 'last_name', 'email')

class ProfileAdmin(admin.ModelAdmin):
    pass
    
