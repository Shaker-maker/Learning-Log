"""Define URL patterns for learning_logs."""
from django.urls import path
from . import views
"""
path function takes three arguments:
1. first argument is a string that help Django route the current request properly
2. second argument - specifies which function to call in views.py
3. provide the name for this URL pattern so we can refer to it in other code sections

"""

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index')
]