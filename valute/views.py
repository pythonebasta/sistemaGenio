
from django.shortcuts import render

def index(request):
    return render(request, 'valute/indexw.html')

from django.shortcuts import render

def index(request):
    return render(request, 'valute/indexw.html', {})

def room(request, room_name):
    return render(request, 'valute/room.html', {
        'room_name': room_name
    })