from django.db import models
from django.conf import settings

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL)
    slug = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
