from django.http import JsonResponse
from rest_framework import exceptions
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, CreateAPIView
from ..models import News
from .serializers import NewsSerializer


class NewsListAPIView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsDetailAPIView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    lookup_field = 'pk'


class NewsDeleteAPIView(DestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    lookup_field = 'pk'


class NewsUpdateAPIView(UpdateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    lookup_field = 'pk'


class NewsCreateAPIView(CreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class VoteApiView(UpdateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def get_queryset(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        news = News.objects.get(pk=pk)
        news.vote +=1
        news.save()







