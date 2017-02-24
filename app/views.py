from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def show(request):
    return render(request, 'show.html')


def user(request, user_id):
    return HttpResponse(user_id)

