from django.contrib.auth.models import User
from django import forms
from django.db import models
from .models import users ,contactus


class UserForm(forms.ModelForm):
    #password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        #contain info about this outer class
        model = users
        fields = ['username','college','email']


class ContactForm(forms.ModelForm):
    #password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        #contain info about this outer class
        model = contactus
        fields = ['name','email','message']


