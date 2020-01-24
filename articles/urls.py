from django.urls import path
from . import views as article_views

urlpatterns = [
    path('', article_views.articles_list, name='articles_index')
]