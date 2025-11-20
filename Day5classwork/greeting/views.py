from django.shortcuts import render

# Create your views here.

from .forms import Loginform

def greeting(request):
    if request.method == 'POST':
        form = Loginform(request.POST)

        # if form.is_valid():
        #     return render (request, 'formdata.html', {
        #     'Formdata' : request.POST,
        #     'Email' : form.email
        #})

        if form.is_valid():
            email = form.cleaned_data['email']
            return render(request, 'formdata.html', {'Email': email})
        return render(request, 'login.html', {'form': form})
    form = Loginform()
    return render(request, 'login.html', {'form' : form})


# def greeting(request):
#     if request.method == 'POST':
#         form = Loginform(request.POST)

#         if form.is_valid():   # <-- This is required
#             email = form.cleaned_data['email']
#             return render(request, 'formdata.html', {"Email": email})

#         # If not valid → return form with errors
#         return render(request, 'login.html', {"form": form})

#     # GET request → blank form
#     form = Loginform()
#     return render(request, 'login.html', {"form": form})
