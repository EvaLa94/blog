from django.urls import path

from . import views

app_name = 'article'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_id>/', views.article_details, name='article_details')
]
