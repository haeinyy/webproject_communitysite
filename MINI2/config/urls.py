from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
     # App
    path('mainpage/', include('mainpage.urls')),
    path('boardapp/', include('boardapp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
