# post/urls.py

from django.urls import path, re_path
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.home_view, name='home'), 
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    re_path(r'^archive/(?P<year>[0-9]{4})/$', views.post_archive),
    path('post/get_post/', views.get_post_handler),  
    path('posts/', views.PostList.as_view()),  
    path('posts/<int:pk>/', views.PostDetail.as_view()),
]
