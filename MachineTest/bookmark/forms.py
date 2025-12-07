from django import forms
from .models import Bookmarks

class Bookmarkform(forms.ModelForm):
    class Meta:
        model = Bookmarks
        fields = ['url', 'title']