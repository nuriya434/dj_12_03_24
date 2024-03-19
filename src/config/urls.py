from django.contrib import admin
from django.urls import path, include
from post.views import home_view, page_404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', include('post.urls')),
    path('', home_view, name='home'),
    path('api/', include('post.urls')),
]

handler404 = page_404
