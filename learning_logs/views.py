from django.shortcuts import render
# import the model associated with the data needed
from .models import Topic
# render function - renders response based on  the data provided in the views

# Create your views here.
def index(request):
    """The Home page for Learning Log."""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """Show all topics"""
    # query DB to get all topics sorted by the date added
    topics = Topic.objects.order_by('date_added')
    # context - we will send it to the template
    """
    a context is a dictionary where keys are the names we'll use in the template to access data
    value - are the data we need to send to the template
    """
    context = {'topics' : topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    """Show a single topic and list all its entries"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic' : topic, 'entries' : entries}
    return render(request, 'learning_logs/topic.html', context)
