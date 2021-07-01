from django.urls import path
from . import views

urlpatterns = [
    path('calcpage/', views.calc, name='calc'),
]