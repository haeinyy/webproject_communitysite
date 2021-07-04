from django.urls import path, include
from boardapp import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'boardapp'

urlpatterns = [
    path('freeboard/', views.freeboard, name='freeboard'),
    path('writetext/', views.writetext, name='writetext'),
    path('<int:pk>/', views.content_view, name='content_view'),
    # path('freeboard/<int:pk>', views.content_view, name='content_view'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)