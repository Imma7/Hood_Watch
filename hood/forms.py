from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Business, NeighbourHood, Profile, Post

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        # fields = ('business_name', 'business_email')
        exclude = ['user']
    

class NeighbourHoodForm(forms.Form):
    class Meta:
        model = NeighbourHood
        exclude = ['occupants']

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['profile']