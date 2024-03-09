from django.contrib import admin
from .models import Article, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    search_fields = ['name']
    prepopulated_fields = {"slug": ("name",)}


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author',
                    'slug', 'category', 'content', 'publish_date', 'update_date']
    search_fields = ['title']
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
