from django.urls import path
from . import views


urlpatterns = [
    # post views
    path(r'^$', views.post_list, name='post_list'),
    path(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'\
        r'(?P<post>[-\w]+)/$',
        views.post_detail,
        name='post_detail'),
]