from django.urls import path
from .views import *

app_name = 'news'


urlpatterns = [
    path('list/', NewsListAPIView.as_view(), name='list'),
    path('detail/<pk>', NewsDetailAPIView.as_view(), name='detail'),
    path('delete/<pk>', NewsDeleteAPIView.as_view(), name='delete'),
    path('update/<pk>', NewsUpdateAPIView.as_view(), name='update'),
    path('create/', NewsCreateAPIView.as_view(), name='create'),

    path('vote/<pk>', VoteApiView.as_view(), name='vote'),

]
