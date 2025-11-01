from django.db import models
from django.utils import timezone


class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-published_date"]

    def __str__(self):
        return self.title

