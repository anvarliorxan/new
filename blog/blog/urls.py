from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/news/', include('news.api.urls',namespace='news')),
    path('api/comments/', include('comments.api.urls',namespace='comments'))
]
