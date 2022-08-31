from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import *


def room(request, room_name):
    # messages = Messages.objects.filter(room=room_name)
    messages = Messages.objects.all()
    context = {'room_name': room_name, 'messages': messages}
    return render(request, 'chatroom.html', context)


def index(request):
    context = {}

    rooms = Chatroom.objects.all()
    context['rooms'] = rooms
    return render(request, 'index.html', context)


def login_request(request):
    # Basic login method
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:  # check if user account is not banned/blocked
                login(request, user)
                return redirect('index')
        else:
            context['message'] = "Invalid username or password."
            return render(request, 'error.html', context)


def logout_request(request):
    # Basic logout method
    logout(request)
    return redirect('index')
