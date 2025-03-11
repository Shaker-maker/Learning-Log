from django.shortcuts import render
# render function - renders response based on  the data provided in the views

# Create your views here.
def index(request):
    """The Home page for Learning Log."""
    return render(request, 'learning_logs/index.html')