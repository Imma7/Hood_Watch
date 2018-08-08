from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .forms import SIgnUpForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from .tokens import account_activation_token
import datetime as dt
from .models import NeighbourHood, Profile, Business

# Create your views here.
def index(request):
    date = dt.date.today()
    hoods = NeighbourHood.all_neighbourhoods()
    return render(request, 'index.html', locals())

def hood(request, id):
    date = dt.date.today()
    hoods = NeighbourHood.objects.get(id=id)
    return render(request, 'hood.html', locals())

def business(request, neighbourhood_id):
    date = dt.date.today()
    business = Business.objects.get(id = neighbourhood_id)
    return render(request, 'hood.html', locals)


def search_results(request):
  if 'hood' in request.GET and request.GET["hood"]:
    search_term = request.GET.get("hood")
    searched_hood = NeighbourHood.search_business(search_term)
    message = f"{search_term}"
    return render(request, 'search.html', {"message": message, "businesses": searched_hood})
  else:
    message = "You haven't searched for any term"
    return render(request, 'search.html', {"message": message})