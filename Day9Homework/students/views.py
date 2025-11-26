from django.shortcuts import render,redirect

# Create your views here.

from .models import Student
from .forms import StudentForm


def home(request):
    return render (request, 'home.html')

def students(request):
    students = Student.objects.all()
    message = "Welcome to "
    return render (request, 'students.html', {
        'students' : students,
        'message' : message
    })

def addstudent(request):
    form = StudentForm()
    
    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('students')
        
    return render (request, 'addstudent.html', {
        'form' : form
    })

