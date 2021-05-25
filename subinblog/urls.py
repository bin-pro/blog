
from django.urls import path
from subinblog.views import base_views, about_views, list_views, post_views

app_name='subinblog'

urlpatterns = [
    path('', base_views.index, name='index'),
    path('about', about_views.about_show, name='about'),
    path('list', list_views.list_show, name='list'),
    path('post', post_views.post_show, name='post'),
]

'''
<!--
{% load static %}
<!doctype html>
<html lang="ko">
    <head>
        <meta charset = "utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link rel="stylesheet" type="text/css" href="{%static 'bootstrap.min.css' %}">
        <link rel="stylesheet" type="text/css" href="{%static 'styles.css'%}">
        <title>Hello, pybo!</title>
    </head>
    <body>
        {% include "navbar.html" %}
        {% block content %}
        {% endblock %}
        <!-- jQuery JS -->
        <script src="{% static 'jquery-3.6.0.min.js' %}"></script>
        <!-- Bootstrap JS-->
        <script src="{% static 'bootstrap.min.js' %}"></script>
        {% block script %}
        {% endblock %}
    </body>
</html>
-->
'''