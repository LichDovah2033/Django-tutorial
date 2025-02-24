from django.shortcuts import render
from django.http import HttpResponse

rooms = [
    {'id': 1, 'name':'This is a message from the student'},
    {'id': 2, 'name':'7 hour videos suck'},
    {'id': 2, 'name':'Please split it up in under 10 minute vidoes let me just read up on it'},
]


# Create your views here.
def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    return render(request, 'base/room.html')