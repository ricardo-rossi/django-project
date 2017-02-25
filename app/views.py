from django.http import HttpResponse
from django.shortcuts import render, redirect
from models import User


# Create your views here.


def index(request):
    return redirect('/main')


def main(request):
    return render(request, 'main.html')


def appointments(request):
    return render(request, 'appointments.html')


# The register() controller creates a new User in the database
def register(request):
    # Get the values entered into the form and put them in variables
    form_name = request.POST['name']
    form_email = request.POST['email']
    form_password = request.POST['password']
    form_dob = request.POST['dob']

    is_valid = User.objects.validate(request.POST)
    return HttpResponse(is_valid)


    # Create a new User by using the User model's create method like this:
    # user = User.objects.create(name=form_name, email=form_email, password=form_password, dob=form_dob)


    # return redirect('/appointments')


def login(request):
    return redirect('/')

# def user(request, user_id):
#     return HttpResponse(user_id)
