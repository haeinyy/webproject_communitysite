from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'calcapp'
urlpatterns = [
    path('donation/', views.donation, name='donation'),
    # 공지사항
    path('notice/', views.notice, name='notice'),
    path('detail/<int:blog_id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('postcreate/', views.postcreate, name='postcreate'),
    path('update/<int:blog_id>/', views.update, name='update'),
    path('delete/<int:blog_id>/', views.delete, name='delete'),
    path('search/', views.search, name='search'),
    path('faq/', views.faq, name='faq'),
    path('suggest/', views.suggest, name='suggest'),
    path('qna/', views.qna, name='qna'),

    # 계산기
    path('calcpage/', views.calcpage, name="calcpage"),
    path('calcpage_result/', views.calcpage_result, name="calcpage_result"),
    
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# calcapp/calcpage/
