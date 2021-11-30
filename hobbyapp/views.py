from django.shortcuts import render
from django.utils import timezone
from django.http.response import HttpResponse, HttpResponseForbidden
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.utils import timezone

from hobbyapp.forms import UserForm
# Create your views here.
def index(request):
    
    return render(request, 'hobbyapp/hobbyapp.html',{
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
            return redirect('index')
        else:
            return HttpResponseForbidden("Invalid credentials")

    return render(request, 'hobbyapp/login.html', {
        'form': UserForm()
    })