from django.urls import path
from restaurant import views


urlpatterns = [
    path('', views.list_1),
]
