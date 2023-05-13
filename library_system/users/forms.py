from multiprocessing import AuthenticationError
from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User



class registerform(UserCreationForm):
    email = forms.CharField()
    first_name=forms.CharField(label="First Name")
    last_name=forms.CharField(label="Last Name ")
    username=forms.CharField(label="User Name")
    registration_number=forms.CharField(label="Registration Number")

    class Meta:
        model = User
        fields = ["first_name","last_name","username","registration_number" , "email" , "password1", "password2"]

