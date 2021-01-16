from django.conf.urls import url,include
from rest_framework import routers

from .views import *

app_name = 'comments'

router = routers.DefaultRouter()
router.register(r'', CommentViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]
