from django.urls import path

from . import views
from . import api

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('', views.login_view, name='login'),
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
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)