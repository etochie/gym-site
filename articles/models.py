from time import time
from django.db import models
from django.utils import timezone

from pytils.translit import slugify


def slug_gen(text):
    """Функция генерации slug для статей
    
    Arguments:
        text {str} -- Любой текст, в нашем случае - название статье
    
    Returns:
        str -- Возвращает строку вида текст-время
    """
    new_slug = slugify(text)
    time_slug = str(int(time()))
    return '{0}-{1}'.format(new_slug, time_slug)


class Article(models.Model):

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField(default="")
    pub_date = models.DateTimeField(default=timezone.now, blank=False)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """Функция сохранения статьи с генерированным slug'ом"""

        if not self.id:
            self.slug = slug_gen(self.title[:20])
        return super().save(*args, **kwargs)


class ArticleStatistic(models.Model):
    """Класс для подсчета кол-ва просмотров статей"""

    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.article.title


    

