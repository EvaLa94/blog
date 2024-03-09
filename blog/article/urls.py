from django.urls import path
from .views import ArticleListView, ArticleDetailView

from . import views

app_name = 'article'
urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('new/', views.add_article, name='add_article'),
    path('<slug:slug>/', ArticleDetailView.as_view(), name='article_detail'),
]
