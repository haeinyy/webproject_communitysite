from django.urls import path, include
from boardapp import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'boardapp'

urlpatterns = [
    # 자유게시판
    path('freeboard/', views.freeboard, name='freeboard'),
    # 동아리/스터디
    path('studyboard/', views.studyboard, name='studyboard'),
    # 취업/진로
    path('jobboard/', views.jobboard, name='jobboard'),
    # 물물교환/무료나눔
    path('tradeboard/', views.tradeboard, name='tradeboard'),
    path('writetext/', views.writetext, name='writetext'),
    path('<int:pk>/', views.content_view, name='content_view'),
    path('<int:pk>/content_delete/', views.content_delete, name='content_delete'),
    path('comment_write/<int:pk>/', views.comment_write, name='comment_write'),
    path('likes/', views.likes, name="likes"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)