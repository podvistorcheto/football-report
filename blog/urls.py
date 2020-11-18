from django.urls import path
from . import views
from .views import (
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView,
    UserArticleListView
)


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('article_list/', ArticleListView.as_view(), name='article_list'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('article/<int:pk>/update/', ArticleUpdateView.as_view(), name='article_update'),
    path('article/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('article/<int:pk>/delete/confirm/', ArticleDeleteView.as_view(), name='article_confirm_delete'),
    path('article/new/', ArticleCreateView.as_view(), name='article_create'),
    path('newsletter/', views.newsletter, name='newsletter'),
]