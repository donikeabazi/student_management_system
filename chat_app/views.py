from django.shortcuts import render

# Create your views here.

rooms = [
    {'id': 1, 'name': 'Lets learn python!'},
    {'id': 2, 'name': 'Design with me'},
    {'id': 3, 'name': 'Frontend developers'},
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'chat_app/home.html', context)

def room(request, roomId):
    room = None
    for i in rooms:
        if i['id'] == int(roomId):
            room = i
    context = {'room': room}
    return render(request, 'chat_app/room.html', context)