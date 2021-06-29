from django import forms
from django.core.exceptions import ValidationError
from .models import Book
from django.contrib.auth.models import User

class Bookform(forms.ModelForm):
    class Meta:
        model=Book
        fields="__all__"

class userform(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password']

