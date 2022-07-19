from cProfile import label
from multiprocessing import context
from pickletools import long4
from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Plot
from django.contrib.auth.forms import UserCreationForm
from .forms import PlotForm

# ****************************
from django.views import generic
from django.contrib.gis.geos import fromstr,Point
from django.core.serializers import serialize

# longitude = -80.191788
# latitude = 25.761681

# my_location = Point(longitude, latitude, srid=4326) 

      
# # Create your views here.
def index(request):
    form = PlotForm()

    context = {'form': form}

    return render(request, 'templates/main/index.html',context)



# def create_plot(request):
#     pass
    
    # if request.method == "POST":
    #     form = PlotForm(request.POST or None)
    #     if form.is_valid():
    #         plot = form.changed_data["plot"]
    #         plot.append(plot)
    #     else:
    #         return render(request, "users/user.html"), {
    #             "form": form
    #         }
    #         form.save()
    #         return redirect ('main/index.html')
    # context = {
    #     "form":form
    # }
#     return render(request, 'templates/main/newplot.html', {
#         "form": PlotForm()
    #})