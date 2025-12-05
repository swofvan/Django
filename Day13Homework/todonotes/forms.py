from django import forms
from .models import Notes

class Add_Notes(forms.ModelForm):
    class Meta:
        model = Notes
        fields = '__all__'