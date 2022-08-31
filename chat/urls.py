from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('<str:room_name>/', room, name='room'),
    path('login', login_request, name='login'),
    re_path(r'.+login[/]*$', login_request, name='login'),
    re_path(r'.+logout[/]*$', logout_request, name='logout'),
]
