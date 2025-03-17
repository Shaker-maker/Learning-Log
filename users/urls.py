"""Defines URL patterns for users"""
from django.urls import path, include

app_name = 'users'

urlpatterns = [
    # Include default authentication URLs
    path('', include('django.contrib.auth.urls')),
]
