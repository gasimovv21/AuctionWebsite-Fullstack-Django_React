from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('users/', views.getUsers, name='users'),
    path('users/<str:pk>', views.getUser, name='user'),
]
