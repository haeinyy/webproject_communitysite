from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'member'

urlpatterns = [
    path('login/', views.login, name='login'),  
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),

    ### 추가된부분 ###
    # 프로필
    path('profile/<int:pk>', views.ProfileView, name='profile'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)