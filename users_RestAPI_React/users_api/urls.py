from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('users/', views.getUsers, name='users'),
    path('users/create/', views.createUser, name='create-user'),
    path('users/<str:pk>/update/', views.updateUser, name='update-user'),
    path('users/<str:pk>/delete/', views.deleteUser, name='delete-user'),

    path('users/<str:pk>', views.getUser, name='user'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
