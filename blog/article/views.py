from django.shortcuts import render, get_object_or_404
from .models import Article
# Create your views here.


def index(request):
    articles_list = Article.objects.all()
    context = {'articles_list': articles_list}
    return render(request, 'index.html', context)


def article_details(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    context = {'article': article}
    return render(request, 'article.html', context)
