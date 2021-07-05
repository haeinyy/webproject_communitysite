from django.urls import path, include
from boardapp import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'boardapp'

urlpatterns = [
    path('freeboard/', views.freeboard, name='freeboard'),
    path('writetext/', views.writetext, name='writetext'),
    path('<int:pk>/', views.content_view, name='content_view'),
    path('<int:pk>/content_delete/', views.content_delete, name='content_delete'),
    path('comment_write/<int:pk>/', views.comment_write, name='comment_write'),
    path('like/', views.like_post, name="like_post"),
    path('post_like_toggle/<int:pk>', views.post_like_toggle, name="post_like_toggle"),
    # path('freeboard/<int:pk>', views.content_view, name='content_view'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)