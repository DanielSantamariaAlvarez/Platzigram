"""Platzigram module"""
from django.contrib import admin
from django.urls import path
from Platzigram import views as view_hello
from posts import views as posts_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', view_hello.hello_world),
    path('posts/', posts_views.list_posts),
]
