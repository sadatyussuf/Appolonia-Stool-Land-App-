# from cProfile import label
# from multiprocessing import context
# from pickletools import long4
# from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Plot
# from django.contrib.auth.forms import UserCreationForm
from .forms import PlotForm

# ****************************
# from django.views import generic
# from django.contrib.gis.geos import fromstr,Point
# from django.core.serializers import serialize

# longitude = -80.191788
# latitude = 25.761681            5.796733790344598, -0.07945842216120023

# my_location = Point(longitude, latitude, srid=4326)  +2330548030734 

      
# # Create your views here.
def index(request):
    # print('............................')
    model_plots = Plot.objects.all()
    # form = PlotForm(request.POST, request.FILES)
    # if request.method == 'POST':
    #     form = PlotForm(request.POST, request.FILES)
    #     print('............................')
    #     print('Request Is POST')
    #     if form.is_valid():
    #         form.save()
    return render(request, 'templates/main/index.html',{'plots':model_plots})



def create_plot(request):
    if request.method == "POST":
        form = PlotForm(request.POST or None, request.FILES or None)
        test = request.FILES['file_upload']
        print(test.read())

    else:
        form = PlotForm()
    return render(request, 'templates/main/newplot.html',{"form":form})