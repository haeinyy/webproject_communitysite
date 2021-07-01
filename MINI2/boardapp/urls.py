from django.urls import path, include
from boardapp import views

urlpatterns = [
    path('', views.freeboard),
]