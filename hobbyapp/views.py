import json
from django.shortcuts import render
from django.utils import timezone
from django.http.response import HttpResponse, HttpResponseForbidden
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone

from hobbyapp.forms import UserForm
from .models import Friend_Request, User,Hobby
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

def friends_view(request):
    
    return render(request, 'hobbyapp/friends.html',{
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


def send_friend_request(request):
    data = json.load(request)
    UserID = data.get('uID')
    from_user = request.user
    to_user = User.objects.get(id=UserID)
    friend_request, created = Friend_Request.objects.get_or_create(
        from_user=from_user, to_user=to_user
    )
    if (created):
        HttpResponse("Friend request sent")
    else:
        HttpResponse("Friend request already sent")

def accept_friend_request(request, requestID):
    friend_request = Friend_Request.objects.get(id=requestID)
    if friend_request.to_user == requestID:
        friend_request.to_user.friends.add(friend_request.from_user)
        friend_request.from_user.friends.add(friend_request.to_user)
        friend_request.delete()
        return HttpResponse("Friend accepted")
    return HttpResponse("Friend not accepted")


