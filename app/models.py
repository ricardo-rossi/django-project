from __future__ import unicode_literals
from django.db import models


class UserManager(models.Manager):
    def validate(self, post_data):
        is_valid = True
        if len(post_data['name']) == 0:
            is_valid = False
        if len(post_data['email']) == 0:
            is_valid = False
        if len(post_data['password']) <= 8:
            is_valid = False
        if post_data['password'] != post_data['confirm_password']:
            is_valid = False
        if len(post_data['dob']) == 0:
            is_valid = False

        return is_valid

    def login(self, post_data):
        # Running a login function!
        # If successful login occurs, maybe return {'theuser':user} where user is a user object?
        # If unsuccessful, maybe return { 'errors':['Login unsuccessful'] }
        pass

    def register(self, post_data):
        # Register a user here"
        # If successful, maybe return {'theuser':user} where user is a user object?
        # If unsuccessful do something like this? return {'errors':['User first name to short', 'Last name too short']
        pass


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
