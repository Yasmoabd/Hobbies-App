from django.urls import path

from . import views
from . import api

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.index, name='index'),
    path('api/user', api.user_api, name='user api'),
    path('api/hobbies', api.hobbies_api, name='hobbies api'),
    path('api/user/city', api.user_city_api, name='user city api'),
    path('api/user/email', api.user_email_api, name='user email api'),
    path('api/user/dob', api.user_dob_api, name='user dob api'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)