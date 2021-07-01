from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainhome),
    path('abc/', views.abc),
]
