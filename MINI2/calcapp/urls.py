from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'calcapp'
urlpatterns = [
    
    # 테스트
    # path('index/', views.index2),

    # 공지사항
    path('home/', views.home, name='home'),
    path('detail/<int:blog_id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('postcreate/', views.postcreate, name='postcreate'),
    path('update/<int:blog_id>/', views.update, name='update'),
    path('delete/<int:blog_id>/', views.delete, name='delete'),
    path('search', views.search, name='search'),
        
    # 연산하는애
    path('calcpage', views.calcpage, name="calcpage"),
    # 연산받는애 : 마이페이지 - 계산기
    path('calcpage_result', views.calcpage_result, name="calcpage_result"),
    # 마이페이지 - 유저정보(수료/수당 현황)
    path('calcpage_result/<str:pk>', views.index),
    # 삭제예정
    path('calcpage_user/', views.calcpage_user, name="calcpage_user"),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
