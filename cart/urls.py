from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add/<id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<id>/', views.remove_from_cart, name='remove_from_cart'),
]
