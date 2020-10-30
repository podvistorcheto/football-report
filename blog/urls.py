from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('blogpage/', views.blogpage, name='blogpage'),
    path('newsletter/', views.newsletter, name='newsletter'),
]