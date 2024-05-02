"""
In many Django projects, especially those that involve user management and authentication,
it is common to extend the capabilities of the default User model provided by Django.
The Profile model is a common pattern used to extend the user model
by adding additional information and functionality specific to the application's requirements.

"""

from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)