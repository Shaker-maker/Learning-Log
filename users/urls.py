"""Defines URL patterns for users"""
from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView
from . views import logout_view

app_name = 'users'

urlpatterns = [
    # Include default authentication URLs
    path('', include('django.contrib.auth.urls')),
    # registration page
    path('register/', views.register, name='register'),
    # logout the usre
    path('users/logout/', logout_view, name='logout'),
]
