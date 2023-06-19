from django.urls import path

from vkr.web import views

urlpatterns = [
    path('contacts', views.contacts),
    path('', views.index),
    path('login', views.login),
    path('anime', views.anime),
    path('animation', views.animation),
]