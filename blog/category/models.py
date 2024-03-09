from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from .utils import slugify_instance


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_instance(instance=self, field=self.name)
        return super().save(*args, **kwargs)


class Article(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL)
    slug = models.SlugField(null=False, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("category:article_detail", kwargs={"category_slug": self.category.slug, "article_slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_instance(instance=self, field=self.title)
        return super().save(*args, **kwargs)
