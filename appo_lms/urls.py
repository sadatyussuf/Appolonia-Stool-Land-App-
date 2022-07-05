
from django import urls
from django.contrib import admin
from django.urls import include, path 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),    
    path("users/", include("users.urls"))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
admin.site.site_header  =  "Appolonia LMS"  
admin.site.site_title  =  "Appolonia LMS Admin Login" 
admin.site.index_title  =  "LMS Admin"
