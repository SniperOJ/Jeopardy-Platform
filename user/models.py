from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    score = models.IntegerField(null=False, default=0)
    email = models.EmailField()