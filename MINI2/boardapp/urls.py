from django.urls import path, include
from boardapp import views
from django.conf import settings
from django.conf.urls.static import static
from .views import Like

app_name = 'boardapp'

urlpatterns = [
    path('freeboard/', views.freeboard, name='freeboard'),
    path('writetext/', views.writetext, name='writetext'),
    path('<int:pk>/', views.content_view, name='content_view'),
    path('comment_write/<int:pk>/', views.comment_write, name='comment_write'),
    path('like/<int:post_id>/', views.like_post, name="like_post"),
    # path('freeboard/<int:pk>', views.content_view, name='content_view'),

    #### 추가 ####
    path('like/<int:board_id>/', Like.as_view(), name="like"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)