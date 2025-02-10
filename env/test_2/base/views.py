from django.shortcuts import render

# Create your views here.
# how do I use the tempalets properly?????

def home(request):
    return render(request, 'home.html')

def DrakeRoom(request):
    return render(request, 'DrakeRoom.html')