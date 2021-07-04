from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

app_name = 'restaurant'

urlpatterns = [
    path('', views.restaurant, name='rest'),
    path('restaurant_list/', views.restaurant_list, name='rest_list'),
    path('restaurant_detail/', views.restaurant_detail, name='rest_detail'),
]