from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('<str:room_name>/', room, name='room'),
    path('signup', signup, name='signup'),
    path('register', register, name='register'),
    path('login', login_request, name='login'),
    path('logout', logout_request, name='logout'),
]
