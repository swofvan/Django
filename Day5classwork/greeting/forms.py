from django import forms
from django.core.validators import validate_email
from django.core.validators import ValidationError

def validate_not_gmail(value):
    if value.find('@gmail') != -1 :
        raise ValidationError(
            "Gmail in not allowed",
            params = {'value' : value},
        )
    
class Loginform (forms.Form):
    email = forms.EmailField(validators = [validate_email, validate_not_gmail])
    password = forms.CharField(min_length = 6)