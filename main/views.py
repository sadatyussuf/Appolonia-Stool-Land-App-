from cProfile import label
from pickletools import long4
from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Plot
from django.contrib.auth.forms import UserCreationForm
# from .models import PlotForm

# class PlotForm(forms.ModelForm):
#     owner = forms.CharField(widget=forms.TextInput(attrs={
#         "class": "form-control",
#         "placeholder": "name"
#     }))
#     address = forms.CharField(widget=forms.TextInput(attrs={
#         "class": "form-control",
#         "placeholder": "owner's address"
#     }))
    
#     plot = forms.CharField(widget=forms.TextInput(attrs={
#         'type': "number",
#         "class": "form-control",
#         "placeholder": "Owner's hometown"
#     }))  
   
#     hometown = forms.CharField(widget=forms.TextInput(attrs={
#         'type': "number",
#         "class": "form-control",
#         "placeholder": "plot coordinates"
#     }))
      
# # Create your views here.
def index(request):
    return render(request, 'templates/users/login.html')



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