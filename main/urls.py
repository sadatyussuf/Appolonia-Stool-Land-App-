from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.index, name="index"),
    path('new_plot/', views.create_plot, name="new_plot"),
]