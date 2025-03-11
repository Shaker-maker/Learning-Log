from django.db import models

# Create your models here.
"""
Each user will need to create a number of topics in their learning log
Each entry will be tied to a topic
These entries will be displayed as text
we will store a timestamp of each entry- to show users when they made the entries
"""

# model -table - tells Django how to work with our data that will be stored in the app
# codewise it is just a class with attributes models

class Topic(models.Model):
    """A topic the user is learnig about"""
    # use CharField - when yu want to store a small amount of text such as name,atitle, city
    text = models.CharField(max_length=200)
    # auto_add_now = True - set attribute to the curent time and date whenever user creates a new opic
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        """Return string represenation of the models"""
        return self.text
    
"""
"""