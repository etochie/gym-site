import pytest
from django.urls import reverse
from django.urls import resolve

from mixer.backend.django import mixer

@pytest.mark.django_db
class TestUrls:

    def test_article_index_url_view_name(self):
        path = reverse('articles_index')
        assert resolve(path).view_name == 'articles_index'

    def test_article_detail_url_view_name(self):
        path = reverse('article_detail', kwargs={'slug': 'test'})
        assert resolve(path).view_name == 'article_detail'

    def test_article_list_url_status_code(self, client):
        path = reverse('articles_index')
        response = client.get(path)
        assert response.status_code == 200

    def test_article_detail_url_status_code(self, client):
        article = mixer.blend('articles.Article')
        path = reverse('article_detail', kwargs={'slug': article.slug})
        response = client.get(path)
        assert response.status_code == 200
