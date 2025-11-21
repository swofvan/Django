from django import forms


class regform(forms.Form):
    Fullname = forms.CharField(min_length = 5, max_length = 50)
    Email = forms.EmailField()
    Password = forms.CharField(min_length = 8, max_length = 20, widget = forms.PasswordInput)