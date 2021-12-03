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
    user = get_object_or_404(User, id=request.user.id)
    return JsonResponse({'user':{
        "dob":user.dateOfBirth,
        "email":user.email,
        "city":user.city,
        "hobbies": [str(h) for h in user.hobbies.all()],
        "image":user.profileImage.url,
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

def user_hobby_api(request):
    if request.method == "PUT":
        user = get_object_or_404(User, id=request.user.id)
        data = json.load(request)
        user.hobbies.clear()
        for hobbyid in data.get('hobbies'):
            user.hobbies.add(Hobby.objects.get(id=hobbyid))
        user.save()
        return JsonResponse({})
    else:
        data = json.load(request)
        h = Hobby(name=data.get('name'))
        h.save()
        return JsonResponse({
        'allHobbies': [
            hobby.to_dict()
            for hobby in Hobby.objects.all()
        ]
    })
