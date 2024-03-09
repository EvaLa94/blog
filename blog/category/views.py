from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Article, Category
from .forms import ArticleForm


class CategoryListView(ListView):
    model = Category
    template_name = "category_list.html"


class CategoryDetailView(DetailView):
    model = Category
    template_name = "category_detail.html"
    slug_url_kwarg = "category_slug"
    slug_field = "slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.get_object()
        context['articles'] = Article.objects.filter(category=category)
        return context


class ArticleListView(ListView):
    model = Article
    template_name = "article_list.html"


class ArticleDetailView(DetailView):
    model = Article
    template_name = "article_detail.html"
    slug_url_kwarg = "article_slug"
    slug_field = "slug"


def add_article(request):
    form = ArticleForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        article = form.save()
        return redirect(article.get_absolute_url())
    return render(request, 'add_article.html', context)
