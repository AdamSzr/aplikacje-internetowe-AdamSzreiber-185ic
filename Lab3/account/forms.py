from django import forms
from django.contrib.auth.models import User



class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class SignUpForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput)