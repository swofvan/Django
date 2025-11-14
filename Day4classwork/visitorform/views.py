from django.shortcuts import render

# Create your views here.

def visitorform(request):
    if request.GET:
        return render(request, 'formdata.html', {
            'form' : request.GET,
        })

    return render(request, 'visitor.html')