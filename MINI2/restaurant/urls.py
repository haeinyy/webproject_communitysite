from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from restaurant import views

urlpatterns = [
    path('', views.restaurant),
    path('restaurant_list/', views.restaurant_list),
    path('restaurant_detail/', views.restaurant_detail),
        #'<str:rest_name>/',
    path('restaurant_search/', views.restaurant_search),
]