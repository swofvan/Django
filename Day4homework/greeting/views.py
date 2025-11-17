from django.shortcuts import render

# Create your views here.

def greeting (request):
    if request.method ==  'POST':
        return render (request, 'formdata.html', {
            'formData' : request.POST,
            'Name' : request.POST.get('name'),
            'color' : request.POST.get('color'),
        })
    return render(request, 'form.html')