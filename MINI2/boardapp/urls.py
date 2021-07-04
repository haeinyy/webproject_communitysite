from django.urls import path, include
# from boardapp import views
from . import views

app_name = 'boardapp'
urlpatterns = [
    path('freeboard/', views.freeboard, name='freeboard'),
    path('writetext/', views.writetext, name='writetext'),
]