from django.shortcuts import render, redirect

# Create your views here.

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def visitcounter(request):
    count = request.session.get('pagecount', 0)
    count += 1
    request.session['pagecount'] = count
    return render (request, 'visitcounter.html', {
        'count' : count
    })

def signup (request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('visitcounter')
        
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
            return redirect('visitcounter')
        
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


# Create a small website where users can sign up and log in. Once logged in, they can visit a “Visit Counter”
# page which shows how many times they have visited that page. Also, add a logout option. The visit counter
# should work only when the user is logged in

