from time import time
import pytest

from pytils.translit import slugify
from mixer.backend.django import mixer
from django.test import RequestFactory
from django.urls import reverse

from articles.views import article_detail


@pytest.mark.django_db
class TestModels:

    def test_article_slug_gen(self):
        title = 'Article title for test'

        test_time = str(int(time()))
        test_slug = '{}-{}'.format(slugify(title[:20]), test_time)

        article = mixer.blend('articles.Article', title=title)
        assert article.slug == test_slug

    def test_article_detail_response(self):
        article = mixer.blend('articles.Article')
        path = reverse('article_detail', kwargs={'slug': article.slug})
        request = RequestFactory().get(path)

        response = article_detail(request, article.slug)
        assert response.status_code == 200

    def test_article_views_counter(self):
        article = mixer.blend('articles.Article')
        views = article.views  # default=0
        path = reverse('article_detail', kwargs={'slug': article.slug})
        request = RequestFactory().get(path)
        response = article_detail(request, article.slug)

        assert article.views > 0
