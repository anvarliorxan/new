from django.contrib.auth.models import User
from django.db import models


class News(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    creation_date = models.DateTimeField(auto_now_add=True)
    vote = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
