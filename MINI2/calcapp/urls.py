from django.urls import path
from . import views

app_name = 'calcapp'
urlpatterns = [
    # 연산하는애
    path('calcpage', views.calcpage, name="calcpage"),
    # 연산받는애 : 마이페이지 - 계산기
    path('calcpage_result', views.calcpage_result, name="calcpage_result"),
    # 마이페이지 - 유저정보
    path('calcpage_user/', views.calcpage_user, name="calcpage_user"),
    # 마이페이지 - 수료/수당 현황
    path('calcpage_info/', views.calcpage_info, name='calcpage_info'),
]
