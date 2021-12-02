from .models import User,Hobby
from django.http import JsonResponse

def user_api(request):
    user = request.user
    return JsonResponse({'user':{
        "dob":user.dateOfBirth,
        "email":user.email,
        "city":user.city,
        "hobbies": [str(h) for h in user.hobbies.all()]
    }})