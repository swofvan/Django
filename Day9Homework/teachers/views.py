from django.shortcuts import render,redirect

# Create your views here.

from .models import Teacher
from .forms import AddTeacher

def teacher (request):
    teachers = Teacher.objects.all()
    message = "Welcome to"

    return render (request, 'teachers.html', {
        'teachers' : teachers,
        'message' : message
    }) 

def addteacher (request):
    form = AddTeacher()

    if request.method == 'POST':
        form = AddTeacher(request.POST)
       
        if form.is_valid():
            form.save()
            return redirect('teacherslist')
        
    return render (request, 'addteacher.html', {
        'form' : form
    })