# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    business = models.BooleanField(default=False)
    entertainment = models.BooleanField(default=False)
    politics = models.BooleanField(default=False)
    world = models.BooleanField(default=False)
    sports = models.BooleanField(default=False)
    health = models.BooleanField(default=False)

    def __str__(self):
        return self.email
