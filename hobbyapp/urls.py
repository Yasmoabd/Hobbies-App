from django.urls import path

from . import views
from . import api


urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('', views.login_view, name='login'),
    path('', views.index, name='index'),
    path('api/user', api.user_api, name='user api'),
]