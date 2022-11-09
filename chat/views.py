from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import *


def room(request, room_name):

    try:
        messages = Messages.objects.filter(room__room_name=room_name)
    except Exception as e:
        print(e)
        room_id = Chatroom.objects.get(room_name=room_name)
        messages = Messages.objects.filter(id=room_id.id)

    context = {'room_name': room_name, 'messages': messages}
    return render(request, 'chatroom.html', context)


def index(request):  # List all chatrooms on the main page
    context = {}

    rooms = Chatroom.objects.all()
    context['rooms'] = rooms
    return render(request, 'index.html', context)


def signup(request):
    context = {}
    return render(request, 'signup.html', context)


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(username, email, password)
        user.save()

        return redirect('index')


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
