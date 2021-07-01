from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
     # App
    path('mainpage/', include('mainpage.urls')),
    
]
