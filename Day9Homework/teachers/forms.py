from django import forms
from .models import Teacher

class AddTeacher (forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'department'] 