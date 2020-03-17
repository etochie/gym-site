from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.views.generic import ListView

from .models import Article, ArticleStatistic


# def articles_list(request):

#     articles = Article.objects.all()

#     return render(request, 'articles/articles_index.html', {
#         'articles': articles
#     })

class ArticleList(ListView):
    template_name = 'articles/articles_index.html'

    def get(self, request, *args, **kwargs):
        last = Article.objects.order_by('-pub_date')
        popular = ArticleStatistic.objects.values('article__title').order_by('views')

        context = {
            'last': last,
            'popular': popular
        }
        return render(request, self.template_name, context=context)



def article_detail(request, slug):

    article = get_object_or_404(Article, slug__iexact=slug)

    obj, created = ArticleStatistic.objects.get_or_create(
        article=article,
        date=timezone.now()
    )
    obj.views += 1
    obj.save()

    return render(request, 'articles/article_detail.html', {
        'article': article,
        'views': obj.views
    })
