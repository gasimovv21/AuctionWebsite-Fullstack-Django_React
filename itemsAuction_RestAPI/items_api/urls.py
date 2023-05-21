from django.urls import path
from . import views


urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('owner_users/', views.getOwnerUsers, name='owner_users'),
    path('users/', views.getUsers, name='users'),
    path('items/', views.getItems, name='items'),
    path('items/<str:pk>', views.getItem, name='item')
]
