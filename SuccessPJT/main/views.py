from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
# Create your views here.

def start(request):
    return render(request, 'start.html')
