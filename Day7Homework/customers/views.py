from django.shortcuts import render

# Create your views here.

from .forms import Custform
from .models import Details

def addcust(request):
    form = Custform()
    
    if request.method == 'POST':
        form = Custform(request.POST)

        if form.is_valid():
            form.save()
            
            customerlist = Details.objects.all()

            return render (request, 'customers.html', {
                'customerlist' : customerlist
            })
        
    return render (request, 'form.html', {
        'form' : form
    })

def all_cust(request):
    customerlist = Details.objects.all().order_by('name')
    return render(request, 'customers.html', {
        'customerlist' : customerlist
    })

def filter(request):
    customerlist = Details.objects.filter(email__endswith = '@example.com').order_by('name')
    return render(request, 'customers.html', {
        'customerlist' : customerlist
    })