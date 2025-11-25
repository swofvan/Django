from django.shortcuts import render, redirect

# Create your views here.

from .models import Student
from .forms import Stuform

def home(request):
    students = Student.objects.all()
    return render (request, 'home.html', {
        'students' : students
    })

def form(request):

    form = Stuform()

    if request.method == 'POST':
        form = Stuform(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    
    return render (request, 'form.html', {
        'form' : form
    })

def result(request, name):
    student = Student.objects.get(name=name)
    return render (request, 'result.html', {
        'student' : student 
    })
