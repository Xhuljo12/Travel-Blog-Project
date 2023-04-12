from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about/', views.about, name='about'),
    path('response/', views.response, name='response'),
    path('contact/', views.contact, name='contact'),
    path('article/', views.article, name='article'),
    path('article/<id>', views.article, name='article'),
    path('articles/', views.articles, name='articles'),
    path('category/<id>', views.category, name='category'),
    path('search/', views.search, name='search'),
]