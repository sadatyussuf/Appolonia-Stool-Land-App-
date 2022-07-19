from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PlotForm(forms.ModelForm):
    owner_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "name"
    }))
    address = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "owner's address"
    }))
    
    # plot = forms.CharField(widget=forms.TextInput(attrs={
    #     'type': "number",
    #     "class": "form-control",
    #     "placeholder": "Owner's hometown"
    # }))  
   
    hometown = forms.CharField(widget=forms.TextInput(attrs={
        'type': "number",
        "class": "form-control",
        "placeholder": "plot coordinates"
    }))
    
    zone = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Zone where plot is located"
    }))
    
    phone_number = forms.CharField(widget=forms.NumberInput(attrs={
        "class": "form-control",
        "placeholder": "Owner's Phone Number"
    }))
    class Meta:
        model = Plot
        # fields = [
        #     'name', 'age','level'
        # ]
        fields = [
            'owner_name', 'address','hometown','zone','phone_number','file_upload'
        ]




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