from django.contrib import admin
from django.urls import path
from restaurant import views

app_name = 'restaurant'

urlpatterns = [
    path('', views.restaurant, name='rest'),
    path('restaurant_list/', views.restaurant_list, name='list'),
    path('<int:pk>/', views.restaurant_detail, name='detail'),
    path('restaurant_search/', views.restaurant_search, name='serach')
        #'<str:rest_url>/',
    # path('restaurant_search/', views.restaurant_search),
]