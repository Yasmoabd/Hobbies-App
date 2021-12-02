import json
from .models import User,Hobby
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

def hobbies_api(request):
    
    return JsonResponse({
        'allHobbies': [
            hobby.to_dict()
            for hobby in Hobby.objects.all()
        ]
    })

def user_api(request):
    user = request.user
    return JsonResponse({'user':{
        "dob":user.dateOfBirth,
        "email":user.email,
        "city":user.city,
        "hobbies": [str(h) for h in user.hobbies.all()]
    }})

def user_city_api(request):
    if request.method == "POST":
        id = request.user.id
        user = get_object_or_404(User, id=request.user.id)
        data = json.load(request)
        user.city=data.get('city')
        user.save()
        return JsonResponse({})

def user_email_api(request):
    if request.method == "POST":
        id = request.user.id
        user = get_object_or_404(User, id=request.user.id)
        data = json.load(request)
        user.email=data.get('email')
        user.save()
        return JsonResponse({})

def user_dob_api(request):
    if request.method == "POST":
        id = request.user.id
        user = get_object_or_404(User, id=request.user.id)
        data = json.load(request)
        user.dateOfBirth=data.get('dob')
        user.save()
        return JsonResponse({})