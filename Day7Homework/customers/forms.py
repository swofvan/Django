from django import forms
from .models import Details

class Custform(forms.ModelForm):
    class Meta:
        model = Details
        fields = ['name', 'email']