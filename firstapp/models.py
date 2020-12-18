from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    id = models.SlugField(primary_key=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(blank=True, null=True)

    def get_absolute_url(self):
        reverse('post-detail', args=[str(self.id)])

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return "postName: " + self.title + " author: " + str(self.author)
