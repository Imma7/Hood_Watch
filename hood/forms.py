from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class BusinessForm(forms.Form):
    business_name = forms.CharField(label='Business Name', max_length=50)
    business_email = forms.EmailField(label='Email')