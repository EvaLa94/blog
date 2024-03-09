from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from .utils import slugify_instance_title


class Article(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL)
    slug = models.SlugField(null=False, unique=True)
    category = models.CharField(max_length=50)
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article:article_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_instance_title(self)
        return super().save(*args, **kwargs)
