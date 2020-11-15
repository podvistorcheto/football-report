from django.urls import path
from . import views
from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView
)


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('article_list/', ArticleListView.as_view(), name='article_list'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('article/new/', ArticleCreateView.as_view(), name='article_create'),
    path('newsletter/', views.newsletter, name='newsletter'),
]