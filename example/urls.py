from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('1/', views.first, name='first'),
    path('2/', views.second, name='second'),
]
