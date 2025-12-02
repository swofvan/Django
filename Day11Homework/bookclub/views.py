from django.shortcuts import render, redirect 

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

from django.contrib.auth.forms import UserCreationForm

@login_required(login_url = 'login')
def welcome(request):
    count = request.session.get('pagecount', 0)
    count += 1
    request.session['pagecount'] = count
    return render (request, 'welcome.html', {
        'count' : count
    })

def signup (request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('welcome')
        
    else:
        form = UserCreationForm()
    
    return render (request, 'signup.html', {
        'form' : form
    })

def loginpage(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('welcome')
        
    else:
        form = AuthenticationForm()
    
    return render (request, 'login.html', {
        'form' : form
    })

@login_required(login_url = 'login')
def logoutpage (request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    
    context = {
        'user' : request.user
    }

    return render (request, 'logout.html', context)


# A local book club wants a simple website where members can sign up and log in. After logging in,
#  each member can see a welcome page that shows how many times they’ve visited the page during their session.

# Your task is to:

# Create a signup page

# Create a login page

# Create a logout functionality

# Create a welcome page that only logged-in users can see

# Show a count of how many times the logged-in user has visited the welcome page during the current session