from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from restaurant import views

app_name = 'restaurant'

urlpatterns = [
    path('', views.restaurant, name='rest'),
    path('restaurant_list/', views.restaurant_list, name='list'),
    path('restaurant_detail/', views.restaurant_detail, name='detail'),
        #'<str:rest_url>/',
    # path('restaurant_search/', views.restaurant_search),
]