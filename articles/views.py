from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Article


def articles_list(request):

    articles = Article.objects.all()

    return render(request, 'articles/articles_index.html', {
        'articles': articles
    })


def article_detail(request, slug):

    article = get_object_or_404(Article, slug__iexact=slug)
    article.views += 1
    article.save()

    return render(request, 'articles/article_detail.html', {
        'article': article
    })
