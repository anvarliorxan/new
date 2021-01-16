from celery import shared_task
from .models import News

@shared_task
def sample_task():
    News.objects.update(vote=0)
    print("Automatically reset everyday")
