from django.shortcuts import render, redirect
# import the model associated with the data needed
from . models import Topic, Entry
from . forms import TopicForm, EntryForm
# allowing users to own their data
from django.contrib.auth.decorators import login_required
from django.http import Http404

# render function - renders response based on  the data provided in the views

# Create your views here.

def index(request):
    """The Home page for Learning Log."""
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """Show all topics"""
    # query DB to get all topics sorted by the date added and their owner only
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    # context - we will send it to the template
    """
    a context is a dictionary where keys are the names we'll use in the template to access data
    value - are the data we need to send to the template
    """
    context = {'topics' : topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """Show a single topic and list all its entries"""
    topic = Topic.objects.get(id=topic_id)
    # make sure the topic belongs to the current user
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic' : topic, 'entries' : entries}
    return render(request, 'learning_logs/topic.html', context)
@login_required
def new_topic(request):
    """
    this function needs to handle two different situations
    1. intial request for the new topic page(show a blank form)
    2.process the data submitted in the form, after processing, redirect users back to the topics page

    """

    # add a new topic
    if request.method != 'POST':
        # No data submitted, create a Blank form
        form = TopicForm()

    else:
        # POST data submitted, process data
        form = TopicForm(data=request.POST)
        if form.is_valid():
            # Asscociating New topics with the currents User
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            # redirect function takes the name and redirects the user to that view
            return redirect('learning_logs:topics')
        
    # Display a blank or invalid form
    context = {'form' : form}
    return render(request, 'learning_logs/new_topic.html', context)




@login_required
def new_entry(request, topic_id):
    """Add a new entry to a paicular topic"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # No data submited, create a blank form

        form = EntryForm()
    else:
        # POST data submitted, process data
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    # Display a blank or invlaid forn
    context = {'topic' : topic, 'form' : form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """When we edit_entry page recieves a GET request, the edit_entry(0 returns a form for editing the entry
    ) when the page receives a POST request with revised entry, it saves the modified txt to the database"""

    # edit an existing entry
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    # make sure only current user can edit
    if topic.owner != request.user:
        raise Http404


    if request.method != 'POST':
        # Initial request, pre-fill form with the curent entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submited; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)


    context = {'entry' : entry, 'topic':topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)

