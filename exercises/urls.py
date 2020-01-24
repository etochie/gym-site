from django.urls import path
from . import views as exercises_views

urlpatterns = [
    path('', exercises_views.exersices_list, name='exercises_index'),
]
