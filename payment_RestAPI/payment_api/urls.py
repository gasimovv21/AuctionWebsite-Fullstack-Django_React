from django.urls import path
from . import views

urlpatterns = [
    path('paypal_detail', views.getPaypalData, name='paypal_detail'),
]
