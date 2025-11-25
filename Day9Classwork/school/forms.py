from django import forms
from .models import Student

class Stuform(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'percentage','result']