from django.shortcuts import render, redirect

# Create your views here.

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render,redirect
from django.contrib.auth import login 

from django.contrib.auth.decorators import login_required
from .forms import Bookmarkform
from .models import Bookmarks

from django.core.paginator import Paginator

from django.db.models import Q

from django.contrib.auth import logout


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()  
            return redirect('add_bookmarks')
   
    else:
        form = UserCreationForm()
   
    return render(request, 'signup.html', {
        'form': form
        })

#----------------------------------------------------------------------------------------------------------

def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('add_bookmarks')
   
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

#----------------------------------------------------------------------------------------------------------

@login_required (login_url='/login/')
def add_bookmarks(request):
    count = Bookmarks.objects.filter(user=request.user).count()   # count user bookmarks

    if count >= 5:
        return render (request, 'error.html', {
            'message' : 'You can only add 5 bookmarks'
        })
    
    if request.method == 'POST':
        form = Bookmarkform(request.POST)
        
        if form.is_valid():
            bookmark = form.save(commit=False)
            bookmark.user = request.user
            bookmark.save()
            return redirect('list_bookmarks')

    else:
        form = Bookmarkform()
    return render (request, 'add_bookmarks.html', {
        'form' : form
    })

#----------------------------------------------------------------------------------------------------------

@login_required(login_url= '/login/')
def list_bookmarks(request):
    search = request.GET.get('q', '')

    bookmarks = Bookmarks.objects.filter(user=request.user)

    # bookmarks = Bookmarks.objects.all()

    if search:
        bookmarks = bookmarks.filter(
            Q(title__icontains=search) |
            Q(url__icontains=search)
        )
    
    paginator = Paginator(bookmarks, 2)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)

    return render (request, 'list.html', {
        'page_obj' : page_obj,
        'search' : search
    })

#----------------------------------------------------------------------------------------------------------

@login_required(login_url='/login/')
def edit_bookmark(request, id):
    bookmark = Bookmarks.objects.get(pk=id)

    if request.method == 'POST':
        form = Bookmarkform(request.POST, instance=bookmark)

        if form.is_valid():
            form.save()
            return redirect ('list_bookmarks')
        
    else:
        form =Bookmarkform(instance=bookmark)
    
    return render (request, 'edit.html', {
            'form' : form
        })

#----------------------------------------------------------------------------------------------------------

@login_required(login_url='/login/')
def dlt_bookmark(request, pk):
    bookmark = Bookmarks.objects.get(pk=pk)
    
    if request.method == 'POST':
        bookmark.delete()
        return redirect(list_bookmarks)
    
    return render (request, 'delete.html', {
        'bookmark' : bookmark
    })

#----------------------------------------------------------------------------------------------------------

@login_required(login_url='/login/')
def logout_page(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    
    context = {
        'user' : request.user
    }

    return render (request, 'logout.html', context)

# Personal Bookmarking Site
# - User can signup in the website
# - Logged in users can add a url and a title
# - The logged in user should be able to add only 5 bookmarks after which it should show an error
# - Logged in users can view the list of urls, along with title and added time
# - The listing page should have pagination
# - Users should be able to search for a particular title/url 
# - Logged in users can edit/delete the urls
# - Logged in users can logout of the website