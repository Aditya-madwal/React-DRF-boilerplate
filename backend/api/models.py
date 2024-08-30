from django.db import models
from users.models import CustomUser
from .logic import *

class Otp(models.Model) :
    email = models.EmailField(max_length=254, unique=True)
    otp = models.CharField(max_length=5, blank=True, null=True)

    def __str__(self):
        return self.email
