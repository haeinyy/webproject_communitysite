from django.contrib import admin
from django.urls import path, include
import calcapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mainpage/', include('mainpage.urls')),
    path('boardapp/', include('boardapp.urls')),
    path('calcapp/', include('calcapp.urls')),
    path('member/', include('member.urls')),
    path('restaurant/', include('restaurant.urls')),

    path('home/', calcapp.views.home, name='home'),
    path('detail/<int:blog_id>', calcapp.views.detail, name='detail'),
]
