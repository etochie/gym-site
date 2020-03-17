import pytest
from mixer.backend.django import mixer
from django.urls import reverse

@pytest.mark.django_db
class TestViews:

    def test_article_views_counter(self, client):
        article = mixer.blend('articles.Article')
        path = reverse('article_detail', kwargs={'slug': article.slug})
        response = client.get(path)
        assert response.context['views'] == 1

    def test_article_list_last_context(self, client):
        article1 = mixer.blend('articles.Article')
        article2 = mixer.blend('articles.Article')
        path = reverse('articles_index')
        response = client.get(path)
        assert response.context['last'][0] == article2

    # def test_article_list_popular_context(self, client):
    #     article1 = mixer.blend('articles.Article', views=1)
    #     article2 = mixer.blend('articles.Article', views=2)
    #     path1 = reverse('article_detail', kwargs={'slug': article1.slug})
    #     path2 = reverse('article_detail', kwargs={'slug': article2.slug})
    #     response1 = client.get(path1)
    #     response2 = client.get(path2)
    #     path = reverse('articles_index')
    #     response = client.get(path)
    #     assert response.context['popular'][0].values('article__title') == article1.title

