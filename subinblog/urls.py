
from django.urls import path
from subinblog.views import base_views

urlpatterns = [

    path('', base_views.index, name='index'),
]