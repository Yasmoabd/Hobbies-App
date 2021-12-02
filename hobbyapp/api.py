import json
from .models import User,Hobby
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

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