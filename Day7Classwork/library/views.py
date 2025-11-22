from django.shortcuts import render

# Create your views here.

from .forms import BookForm
from .models import Books

def library(request):
    form = BookForm()

    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()

            booklist = Books.objects.all()

            return render(request, 'booklist.html', {
                'booklist' : booklist
            })

    return render(request, 'form.html', {
        'form': form
        })


def booklist(request):
    booklist = Books.objects.all()
    return render(request, 'booklist.html', {
        'booklist': booklist
        })
