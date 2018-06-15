from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(max_length=0x20, null=False, default="", unique=True)
    score = models.PositiveIntegerField(null=False, default=0)
    university = models.CharField(max_length=0x20, null=False, default="")
    email = models.EmailField(unique=True)
    register_ip = models.GenericIPAddressField()
    active_code = models.CharField(max_length=0x20, null=True)
    destroyed = models.BooleanField(default=False)
    blocked = models.BooleanField(default=False)


class LoginLog(models.Model):
    time = models.DateTimeField(auto_now=True)
    username = models.CharField(max_length=0x400)
    password = models.CharField(max_length=0x400)
    captcha = models.CharField(max_length=0x10)
    ip = models.GenericIPAddressField()
    user_agent = models.CharField(max_length=0x400)
