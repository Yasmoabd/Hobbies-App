import datetime
import json
from .models import User,Hobby
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
import dateutil.relativedelta

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

def test_api():
    arr=[]
    return JsonResponse({
        'best':[
            {
                'matches':b.matches
            }
            for b in arr
        ]
    })

def hobby_match_api(request):
    user = get_object_or_404(User, id=request.user.id)
    matches=[]
    for otherUser in User.objects.all():
        matchCount = 0
        matchingHobbies = []
        for userHobby in otherUser.hobbies.all():
            if userHobby in user.hobbies.all():
                matchCount+=1
                matchingHobbies.append(str(userHobby))
        matches.append((matchCount,otherUser.username,matchingHobbies))
    matches = sorted(matches, key=lambda x: x[0],reverse=True)
    return JsonResponse({
        'matches':[
            {
                'numOfMatches':b[0],
                'name':b[1],
                'hobbies':b[2],
            }
            for b in matches
        ]
    })

def filter(request):
    data=json.load(request)
    if(data.get('city')=="none"):
        cityFilter = None
    else:
        cityFilter=data.get('city')
    
    if int(data.get('upper'))<0:
        ageFilter = -1
    else:
        ageFilter=int(data.get('upper'))
    print(ageFilter,cityFilter)
    if(ageFilter==-1 and cityFilter==None):
        return hobby_match_api(request)
    else:
        filteredUsers = []
        if cityFilter!=None:
            filteredByCity = User.objects.filter(city=data.get('city'))
            print(filteredByCity)
            for otherUser in filteredByCity:
                filteredUsers.append(otherUser.username)
        
        if ageFilter>0:
            lower = int(data.get('lower'))
            upper = int(data.get('upper'))
            print(upper,lower)
            for otherUser in User.objects.all():
                datetime1 = otherUser.dateOfBirth
                datetime2 = datetime.datetime.now()
                time_difference = dateutil.relativedelta.relativedelta(datetime2, datetime1)
                difference_in_years = time_difference.years
                if(difference_in_years>lower and difference_in_years<=upper):
                    filteredUsers.append(otherUser.username)
    return JsonResponse({
        'matches':[
            {
                'name': b
            }
            for b in filteredUsers
        ]
    })
