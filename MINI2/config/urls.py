from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from restaurant import views as rest_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/', rest_views.list_1),
]
