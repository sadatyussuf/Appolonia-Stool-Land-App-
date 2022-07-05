from django.urls import path
from . import views
from django.contrib import admin
from .views import home_view, signup_view


app_name = "users"

urlpatterns = [
    path('', views.index, name="index"),
    path('signup/', signup_view, name="signup"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.logout_view, name="logout"),    
    path("property/", views.property_single, name="property-single"),        
    path("properties/", views.property_grid, name="property-grid"),
    path("agent/", views.agent_single, name="agent-single"),
    path("agents/", views.agent_grid, name="agent-grid"),
    path("contact/", views.contact, name="contact"),
    path("blog/", views.blog_single, name="blog-single"),
    path("blogs/", views.blog_grid, name="blog-grid"),
    
]