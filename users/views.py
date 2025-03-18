from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    """Register a new user"""
    if request.method != 'POST':
        # create a new form
        form = UserCreationForm()
    else:
        # process the completed foem
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # login the user and redirect them to home page
            login(request, new_user)
            return redirect('learning_logs:index')
        
    
    # display a blank or invlaid form
    context = {'form' : form}
    return render(request, 'registration/register.html', context)



def logout_view(request):
    # log the use out
    logout(request)
    return redirect('learning_logs:index')


    
