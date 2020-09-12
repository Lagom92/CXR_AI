from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.test, name='test'),
    path('result/', views.result, name='result'),
    path('detect/', views.detect, name='detect'),
    
]