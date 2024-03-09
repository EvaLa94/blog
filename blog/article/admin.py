from django.contrib import admin
from .models import Article

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author',
                    'slug', 'category', 'content', 'publish_date', 'update_date']
    search_fields = ['title']
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Article, ArticleAdmin)
