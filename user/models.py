from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(max_length=0x20, null=False, default="未知")
    score = models.PositiveIntegerField(null=False, default=0)
    university = models.CharField(max_length=0x20, null=False, default="未知")
    email = models.EmailField()
    register_ip = models.GenericIPAddressField(null=False, default="127.0.0.1")
    active_code = models.CharField(max_length=0x20, null=True)
