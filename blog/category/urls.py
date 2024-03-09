from django.urls import path
from .views import ArticleListView, ArticleDetailView, CategoryListView, CategoryDetailView

from . import views

app_name = 'category'
urlpatterns = [
    path('', CategoryListView.as_view(), name='category_list'),
    path('new-article/', views.add_article, name='add_article'),
    path('articles/', ArticleListView.as_view(), name='article_list'),
    path('<slug:category_slug>/',
         CategoryDetailView.as_view(), name='category_detail'),
    path('<slug:category_slug>/article/<slug:article_slug>/',
         ArticleDetailView.as_view(), name='article_detail'),

]
