from django.urls import path
from . import views

app_name = 'calcapp'
urlpatterns = [
    
    # 테스트
    path('test/', views.test, name='test'),

    # 공지사항
    path('notice/', views.notice, name='notice'),
    path('detail/<int:blog_id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('postcreate/', views.postcreate, name='postcreate'),
    path('update/<int:blog_id>/', views.update, name='update'),
    path('delete/<int:blog_id>/', views.delete, name='delete'),
    path('search', views.search, name='search'),
    path('faq', views.faq, name='faq'),
    path('suggest', views.suggest, name='suggest'),
    path('qna', views.qna, name='qna'),

        
    # 연산하는애
    path('calcpage', views.calcpage, name="calcpage"),
    # 연산받는애 : 마이페이지 - 계산기
    path('calcpage_result', views.calcpage_result, name="calcpage_result"),
    # 마이페이지 - 유저정보
    path('calcpage_user/', views.calcpage_user, name="calcpage_user"),
    # 마이페이지 - 수료/수당 현황
    path('calcpage_info/', views.calcpage_info, name='calcpage_info'),
    path('calcpage_info/<str:pk>', views.index),

]
