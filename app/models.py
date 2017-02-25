from __future__ import unicode_literals
from django.db import models


class UserManager(models.Manager):
    def validate(self, post_data):
        is_valid = True
        # Check that 'name' is not empty
        if len(post_data['name']) == 0:
            is_valid = False
        # Check that 'email' is not empty
        if len(post_data['email']) == 0:
            is_valid = False
        # Check that 'password' length is not less than 8 chars
        if len(post_data['password']) < 8:
            is_valid = False
        # Check that 'password' and 'confirm_password' are not different
        if post_data['password'] != post_data['confirm_password']:
            is_valid = False
        # Check that 'dob' is not empty
        if len(post_data['dob']) == 0:
            is_valid = False

        return is_valid

    def login(self, post_data):
        # Running a login function!
        # If successful login occurs, maybe return {'theuser':user} where user is a user object?
        # If unsuccessful, maybe return { 'errors':['Login unsuccessful'] }
        pass

    def register(self, post_data):
        # Register a user here
        # Get the values entered into the form and put them in variables
        form_name = post_data['name']
        form_email = post_data['email']
        form_password = post_data['password']
        form_dob = post_data['dob']

        # Create a new User by using the User model's create method like this:
        user = User.objects.create(name=form_name, email=form_email, password=form_password, dob=form_dob)

        return user


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    dob = models.DateTimeField()

    # *************************
    # Connect an instance of UserManager to our User model overwriting
    # the old hidden objects key with a new one with extra properties!!!
    objects = UserManager()
    # *************************
