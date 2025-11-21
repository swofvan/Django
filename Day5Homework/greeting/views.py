from django.shortcuts import render

# Create your views here.

from .forms import regform

def greeting(request):
    if request.method == 'POST':
        form = regform(request.POST)

        if form.is_valid():
            name = form.cleaned_data['Fullname']
            return render(request, 'formdata.html', {
                'name' : name
            })
        
        return render (request, "form.html", {'form' : form})
    
    form = regform()
    return render (request, "form.html", {
        'form' : form
    })
            