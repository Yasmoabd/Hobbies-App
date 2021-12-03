from django.shortcuts import render
from django.utils import timezone
from django.http.response import HttpResponse, HttpResponseForbidden
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone

from hobbyapp.forms import UserForm
from .models import User,Hobby
# Create your views here.
def matches_view(request):
    return render(request, 'hobbyapp/matches.html',{
        'title': "Hobbies App",
    })

def profile_view(request):
    return render(request, 'hobbyapp/hobbyapp.html',{
        'title': "Hobbies App",
    })


def home_view(request):
    
    return render(request, 'hobbyapp/home.html',{
        'title': "Hobbies App",
    })

def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password'],
        )
        if user is not None:
            login(request, user)
            return home_view(request)
        else:
            return HttpResponseForbidden("Invalid credentials")

    return render(request, 'hobbyapp/login.html', {
        'form': UserForm()
    })

def logout_view(request):
    logout(request)
    return login_view(request)

def signup_view(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return home_view(request)
    return render(request, 'hobbyapp/signup.html', {
        'form': form,
    })



