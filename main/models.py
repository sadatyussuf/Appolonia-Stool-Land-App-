from django.contrib.gis.db import models
from django.core.validators import RegexValidator
from django.urls import reverse
from django.contrib.gis.db import models as gis_models
from django.contrib.gis.geos import  Polygon



# Create your models here.

class Plot(models.Model):
    owner_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    hometown = models.CharField(max_length=54)
    zone = models.CharField(max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,13}$', message="Phone number must be entered in the format: '+999999999'. Up to 13 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # Validators should be a list
    plot = models.PolygonField() #! will remove this later
    geom = models.MultiPolygonField(null=True)
    class Meta:
        verbose_name = "Plot"
        verbose_name_plural = "Plots"
    def __str__(self):
        return f'{ self.owner_name } { self.geom }'