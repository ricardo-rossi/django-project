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
    # Check the validity of the form data - validate() is in UserManager (file models.py)
    error = User.objects.validate(request.POST)

    if error:
        # Render form again passing the validation error to it
        return render(request, 'main.html', {'error': error})
    else:
        # Passed validation so register the user
        User.objects.register(request.POST)
        # Redirect to next page
        return redirect('/appointments')


def login(request):
    return redirect('/')

# def user(request, user_id):
#     return HttpResponse(user_id)
