
from django.shortcuts import render, redirect
from .models import Plot
from .forms import PlotForm

from csv import DictReader
from io import TextIOWrapper
# longitude = -80.191788
# latitude = 25.761681     

# my_location = Point(longitude, latitude, srid=4326)  

      
# # Create your views here.
def index(request):
    model_plots = Plot.objects.all()

    return render(request, 'templates/main/index.html',{'plots':model_plots})


def create_plot(request):
    if request.method == "POST":
        form = PlotForm(request.POST or None, request.FILES or None)

        test = request.FILES['file_upload']
        rows = TextIOWrapper(test,encoding='utf-8',newline="")
        for row in DictReader(rows):
            print(row)
 

    else:
        form = PlotForm()
    return render(request, 'templates/main/newplot.html',{"form":form})



   # form = PlotForm(request.POST, request.FILES)
    # if request.method == 'POST':
    #     form = PlotForm(request.POST, request.FILES)
    #     print('............................')
    #     print('Request Is POST')
    #     if form.is_valid():
    #         form.save()