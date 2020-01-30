from django.urls import path
from . import views as article_views

urlpatterns = [
    path('', article_views.articles_list, name='articles_index'),
    path('<str:slug>', article_views.article_detail, name='article_detail'),
]
