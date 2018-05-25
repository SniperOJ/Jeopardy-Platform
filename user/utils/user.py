from django.contrib.auth.backends import ModelBackend
from django.http import JsonResponse
from django.db.models import Q

from ..models import User

from functools import wraps
import hashlib
import string
import random


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(
                Q(username=username) | Q(email=username)
            )
            if user.check_password(password):
                return user
        except Exception as e:
            return None


def md5(data):
    return hashlib.md5(data).hexdigest()


def random_string(charset, length):
    return "".join([random.choice(charset) for i in range(length)])


def generate_active_code():
    length = 0x20
    return random_string(string.ascii_letters + string.digits, length)

# def login_required(func):
#     @wraps(func)
#     def returned_wrapper(request, *args, **kwargs):
#         if not check_login(request):
#             result = {
#                 "status": False,
#                 "result": "You can not do this before loged in! Please login!"
#             }
#             return JsonResponse(result)
#         else:
#             return func(request, *args, **kwargs)
#
#     return returned_wrapper
#
#
# def clear_session(func):
#     @wraps(func)
#     def returned_wrapper(request, *args, **kwargs):
#         request.session.clear()
#         return func(request, *args, **kwargs)
#
#     return returned_wrapper
