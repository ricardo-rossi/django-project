from __future__ import unicode_literals

import bcrypt
import re
from django.db import models


class UserManager(models.Manager):
    def validate(self, post_data):
        error = ""
        # Check that 'name' is not empty
        if len(post_data['name']) == 0:
            error = "Please provide a Name"
        # Check that 'email' is not empty
        elif len(post_data['email']) == 0:
            error = "Please provide an Email"
        elif not re.match(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$", post_data['email']):
            error = "Not a valid Email"
        # Check that 'password' length is not less than 8 chars
        elif len(post_data['password']) < 8:
            error = "Please enter a Password with at least 8 characters"
        # Check that 'password' and 'confirm_password' are not different
        elif post_data['password'] != post_data['confirm_password']:
            error = "Password and Confirmation Password must match"
        # Check that 'dob' is not empty
        elif len(post_data['dob']) == 0:
            error = "Please provide a Date of Birth"

        # Return the error if any
        return error

    def login(self, post_data):
        # Attempting to login a user
        # Get the values entered into the form and put them in variables
        form_email = post_data['email']
        form_password = post_data['password']
        # Lookup the user
        user = User.objects.filter(email=form_email)

        if user.count() > 0 and bcrypt.checkpw(form_password.encode(), user[0].password.encode()):
            # Return the logged in user
            return {'error': '', 'user': user[0]}

        # Can't find user. Return error
        return {'error': 'Login unsuccessful'}

    def register(self, post_data):
        # Register a user here
        # Get the values entered into the form and put them in variables
        form_name = post_data['name']
        form_email = post_data['email']
        form_password = post_data['password']
        form_dob = post_data['dob']
        # Encrypt the password
        bcrypt_password = bcrypt.hashpw(form_password.encode(), bcrypt.gensalt())
        # Create a new User by using the User model's create method like this:
        user = User.objects.create(name=form_name, email=form_email, password=bcrypt_password, dob=form_dob)

        # Returned the registered user
        return user


class User(models.Model):
    # Define all fields in the User model
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    dob = models.DateTimeField()
    # The line below connects UserManager to this User model
    # so that access things like User.objects.validate()
    objects = UserManager()
