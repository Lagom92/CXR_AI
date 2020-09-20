from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('test/', views.test, name='test'),
    path('result/', views.result, name='result'),
    path('model/', views.model, name='model'),
]