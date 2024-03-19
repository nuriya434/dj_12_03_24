from django.urls import path, re_path
from .views import home_view, post_detail, post_archive, get_post_handler, PostDeleteView

app_name = 'post'

urlpatterns = [
    path('', home_view, name='home'), 
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    re_path(r'^archive/(?P<year>[0-9]{4})/$', post_archive),
    path('post/get_post/', get_post_handler),  
    path('<int:pk>/', post_detail, name='post-detail'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]