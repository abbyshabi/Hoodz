from django import forms
from django.contrib.auth.models import User
from django.core import validators
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import Profile,Business,Project,Post

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['owner']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude=['admin']
     