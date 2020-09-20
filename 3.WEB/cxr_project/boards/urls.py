from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('test/', views.test, name='test'),
    path('result/', views.result, name='result'),
    path('model/', views.model, name='model'),
    path('history/<int:user_id>/', views.history, name='history'),
    path('history/<int:user_id>/deatil/<int:id>/', views.detail, name='detail'),
    path('visualizationel/', views.visualization, name='visualization'),
]
