from django.urls import path
from . import views as article_views

urlpatterns = [
    path('', article_views.ArticleList.as_view(), name='articles_index'),
    path('articles/<str:slug>/', article_views.article_detail, name='article_detail'),
]
