from django.shortcuts import render

# Create your views here.

from .forms import Loginform

def greeting(request):
    if request.method == 'POST':
        form = Loginform(request.POST)    

        if form.is_valid():
            email = form.cleaned_data['email']
            return render(request, 'formdata.html', {'Email': email})
        return render(request, 'login.html', {'form': form})
    
    form = Loginform()
    return render(request, 'login.html', {
        'form' : form
        })