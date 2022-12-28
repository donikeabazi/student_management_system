from django.shortcuts import render
from .models import Room

# Create your views here.

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'chat_app/home.html', context)

def room(request, roomId):
    room = Room.objects.get(id=roomId)
    context = {'room': room}
    return render(request, 'chat_app/room.html', context)