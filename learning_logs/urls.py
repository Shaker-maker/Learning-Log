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
    path('', views.index, name='index'),
    # for all topics
    path('topics/', views.topics, name='topics'),
    # Detail page for a single topic
    path('topics<int:topic_id>/', views.topic, name='topic'),
    # a page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # a page for adding a new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # a page to edit entries
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]