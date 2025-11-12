from django.shortcuts import render

# Create your views here.

# from django.http import HttpResponse

def greeting(request):
    return render(request, 'home.html')

def aboutus(request):
    return render(request, 'aboutus.html')