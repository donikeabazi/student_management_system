from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import get_user_model
# from django.contrib import messages
from django.db.models import Q
from .models import Message, Room, Topic
from .forms import RoomForm

# Create your views here.

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(description__icontains=q) |
        Q(name__icontains=q)
        )
    topics = Topic.objects.all()
    room_count = rooms.count()
    room_messages = Message.objects.filter(Q(room__topic__name__icontains=q))

    context = {
        'rooms': rooms,
        'topics': topics,
        'room_count': room_count,
        'room_messages': room_messages,
        }
    return render(request, 'chat_app/home.html', context)

def room(request, id):
    room = Room.objects.get(id=id)
    room_messages = room.message_set.all().order_by('-created_at')
    participants = room.participants.all()
    if request.method == 'POST':
        Message.objects.create(
            user = request.user,
            room = room,
            body = request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room', id=room.id)

    context = {
        'room': room,
        'room_messages': room_messages,
        'participants': participants
    }
    return render(request, 'chat_app/room.html', context)

def profile(request, id):
    user = get_user_model().objects.get(id=id)
    rooms = user.room_set.all()
    room_messages = user.message_set.all()
    topics = Topic.objects.all()

    context = {
        'user': user,
        'rooms': rooms,
        'topics': topics,
        'room_messages': room_messages,
    }
    return render(request, 'chat_app/profile.html', context)

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'chat_app/room_form.html', context)

def updateRoom(request, id):
    room = Room.objects.get(id = id)
    form = RoomForm(instance=room)

    if request.user != room.host:
        return HttpResponse('You are not allowed here')

    if request.method == 'POST':
            form = RoomForm(request.POST, instance=room)
            if form.is_valid():
                form.save()
                return redirect('home')

    context = {'form': form}
    return render(request, 'chat_app/room_form.html', context)

def deleteRoom(request, id):
    room = Room.objects.get(id = id)

    if request.user != room.host:
        return HttpResponse('You are not allowed here')

    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'chat_app/delete.html', {'obj': room})

def deleteMessage(request, id):
    message = Message.objects.get(id = id)

    if request.user != message.user:
        return HttpResponse('You are not allowed here')

    if request.method == 'POST':
        message.delete()
        return redirect('room', id=message.room.id)
    return render(request, 'chat_app/delete.html', {'obj': message})
