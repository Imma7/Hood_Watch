from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .forms import NeighbourHoodForm, BusinessForm, NewProfileForm
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
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    date = dt.date.today()
    hoods = NeighbourHood.all_neighbourhoods()
    return render(request, 'index.html', locals())

@login_required(login_url='/accounts/login/')
def hood(request, id):
    date = dt.date.today()
    hoods = NeighbourHood.objects.get(id=id)
    return render(request, 'hood.html', locals())

@login_required(login_url='/accounts/login/')
def business(request, hood_id):
    date = dt.date.today()
    print(date)
    bs = Business.objects.filter(neighbourhood_id=hood_id)
    print(bs)
    return render(request, 'hood.html', locals())

@login_required(login_url='/accounts/login/')
def search_results(request):
  if 'hood' in request.GET and request.GET["hood"]:
    search_term = request.GET.get("hood")
    searched_hood = NeighbourHood.search_business(search_term)
    message = f"{search_term}"
    return render(request, 'search.html', {"message": message, "businesses": searched_hood})
  else:
    message = "You haven't searched for any term"
    return render(request, 'search.html', {"message": message})

@login_required(login_url='/accounts/login/')
def new_biz(request):
    current_user = request.user
    if request.method == 'POST':
        print(1)
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            print('valid')
            nusu=form.save(commit=False)
            nusu.user = current_user
            nusu.neighbourhood = current_user.profile_for.neighbourhood
            nusu.save()
            return redirect('index')
    else:
        form = BusinessForm()
    return render(request, "new_biz.html", {"form":form})

def new_profile(request):
    current_user = request.user

    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES, instance = current_user.profile_for)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
            return redirect('index')
    else:
        form = NewProfileForm()
    return render(request, 'new_profile.html', {"form": form})


def biz_in_hood(request, neighbourhood_id):
    bizs = Business.objects.filter(neighbourhood_id=neighbourhood_id)
    return render(request, 'hood.html', locals())

def new_post(request):
    current_user = request.user

    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            return redirect('index')
    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {"form": form})