from django.urls import path

from vkr.web import views

urlpatterns = [
    path('contacts', views.contacts),
    path('index', views.index),
    path('animation', views.animation),
    path('login', views.login),
]