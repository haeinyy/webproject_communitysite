from django.contrib import admin
from django.urls import path, include
import calcapp.views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('mainpage/', include('mainpage.urls')),
    path('boardapp/', include('boardapp.urls')),
    path('calcapp/', include('calcapp.urls')),
    path('member/', include('member.urls')),
    path('restaurant/', include('restaurant.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
