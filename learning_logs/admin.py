from django.contrib import admin

# Register your models here.
"""
to register a model do the following
1. import it 
2. reister it
"""
from . models import Topic, Entry
admin.site.register(Topic)
admin.site.register(Entry)~