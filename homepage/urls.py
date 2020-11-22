from django.urls import path
from . import views


urlpatterns = [
    path('article/<int:pk>/', views.home, name='index')
]