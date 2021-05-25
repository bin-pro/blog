
from django.urls import path
from subinblog.views import base_views, about_views, list_views, post_views

app_name='subinblog'

urlpatterns = [
    path('', base_views.index, name='index'),
    path('about', about_views.about_show, name='about'),
    path('list', list_views.list_show, name='list'),
    path('post', post_views.post_show, name='post'),
]