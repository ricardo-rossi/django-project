from django.http import HttpResponse
from django.shortcuts import render, redirect
from models import User


# Create your views here.


def index(request):
    return render(request, 'index.html')


# The register() controller creates a new User in the database
def register(request):
    # Check the validity of the form data - validate() is in UserManager (file models.py)
    error = User.objects.validate(request.POST)

    if error:
        # Render form again passing the validation error to it
        return render(request, 'index.html', {'error': error})
    else:
        # Passed validation so register the user
        user = User.objects.register(request.POST)
        # Store registered user in session
        request.session['user_id'] = user.id
        # Redirect to next page
        return redirect('/appointments')


def login(request):
    # Attempt to login
    response = User.objects.login(request.POST)

    if len(response['error']) > 0:
        return HttpResponse(response['error'])
    else:
        # Store logged in user in session
        request.session['user_id'] = response['user'].id
        return redirect('/appointments')


def appointments(request):
    if request.session is not None:
        return render(request, 'appointments.html')
    else:
        return redirect('/')

# def user(request, user_id):
#     return HttpResponse(user_id)
