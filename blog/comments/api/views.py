from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import CommentsSerializer
from ..models import Comments


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
