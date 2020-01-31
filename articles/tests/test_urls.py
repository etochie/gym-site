from django.urls import reverse
from django.urls import resolve


class TestUrls:

    def test_article_index_url(self):
        path = reverse('articles_index')
        assert resolve(path).view_name == 'articles_index'

    def test_article_detail_url(self):
        path = reverse('article_detail', kwargs={'slug': 'test'})
        assert resolve(path).view_name == 'article_detail'
