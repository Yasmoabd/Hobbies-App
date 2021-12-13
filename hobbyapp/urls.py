from django.urls import path

from . import views
from . import api

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('', views.login_view, name='login'),
    path('friends/', views.friends_view, name='friends'),
    path('logout/', views.logout_view, name='logout'),

    path('home/', views.home_view, name='index'),
    path('profile/', views.profile_view, name='profile'),
    path('matches/', views.matches_view, name='matches'),
    path('filter/', api.filter, name='filter'),
    

    path('api/user', api.user_api, name='user api'),
    path('api/hobbies', api.hobbies_api, name='hobbies api'),
    path('api/user/city', api.user_city_api, name='user city api'),
    path('api/user/email', api.user_email_api, name='user email api'),
    path('api/user/dob', api.user_dob_api, name='user dob api'),
    path('api/user/hobby', api.user_hobby_api, name='user hobbies api'),
    path('api/hobbymatch', api.hobby_match_api, name='hobbymatch api'),
    path('api/friends', api.friends_api, name='friends api'),
    path('api/friendreq', api.friend_requests_api, name='friend request api'),
    path('api/addfriend', api.add_friend_api, name='add friend api'),

    path('send_friend_request', views.send_friend_request, name='send friend request'),
    path('accept_friend_request', views.accept_friend_request, name='accept friend request'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)