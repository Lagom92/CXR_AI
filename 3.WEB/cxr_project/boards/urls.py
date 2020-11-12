from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('test/', views.test, name='test'),
    path('result/', views.result, name='result'),
    
    path('model/', views.model, name='model'),
    path('history/<int:user_id>/', views.history, name='history'),
    path('history/<int:user_id>/deatil/<int:id>/', views.detail, name='detail'),
    path('delete/<int:user_id>/<int:id>/', views.delete, name='delete'),
    path('visualization/', views.visualization, name='visualization'),
    path('member/', views.member, name='member'),


    path('audiotest/', views.audiotest, name='audiotest'),
    path('audioresult/', views.audioresult, name='audioresult'),


    path('multitest/', views.multitest, name='multitest'),
    path('multiresult/', views.multiresult, name='multiresult'),

]
