from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Business, NeighbourHood, Profile

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        # fields = ('business_name', 'business_email')
        exclude = ['user']
    

class NeighbourHoodForm(forms.Form):
    neighbourhood_name = forms.CharField(label='Neighbourhood Name', max_length = 50)
    neighbourhood_location = forms.CharField(label='Location', max_length = 50)
    occupants = forms.IntegerField(label='Occupants')

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']