from django.urls import path, include
from boardapp import views

urlpatterns = [
    path('freeboard/', views.freeboard),
    path('writetext/', views.writetext),
    path('ddd/', views.ddd),
]