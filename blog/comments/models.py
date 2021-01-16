from django.contrib.auth.models import User
from django.db import models
from news.models import News


class Comments(models.Model):

    author = models.ForeignKey(User,on_delete=models.CASCADE)
    news = models.ForeignKey(News,on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    creation_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.author.username

