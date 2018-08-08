from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class BusinessForm(forms.Form):
    business_name = forms.CharField(label='Business Name', max_length=50)
    business_email = forms.EmailField(label='Email')

class NeighbourHoodForm(forms.Form):
    neighbourhood_name = forms.CharField(label='Neighbourhood Name', max_length = 50)
    neighbourhood_location = forms.CharField(label='Location', max_length = 50)
    occupants = forms.IntegerField(label='Occupants')