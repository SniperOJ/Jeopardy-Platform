#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Import Django Lib
from django.http import JsonResponse
from django.utils.translation import ugettext as _
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password

# Import Project Lib
from user.utils.form import check_params
from user.utils.user import generate_active_code

from .models import User

from django.contrib.auth import authenticate as django_authenticate
from django.contrib.auth import login as django_login


# Import System Lib


@check_params(["username", "password"])
def login(request):
    # Actually `username` can represent nickname and email
    username = str(request.POST['username'])
    password = str(request.POST['password'])

    # Authenticate
    user = django_authenticate(username=username, password=password)

    # Generate Response
    if user:
        # Check destroyed
        if user.destroyed:
            result = {
                "status": False,
                "result": _("User destroyed!")
            }
            return JsonResponse(result)
        # Check is_active
        if not user.is_active:
            result = {
                "status": False,
                "result": _("User is not active!")
            }
            return JsonResponse(result)
        # Check Blocked
        if user.blocked:
            result = {
                "status": False,
                "result": _("User blocked!")
            }
            return JsonResponse(result)
        # Set session
        django_login(request, user)
        result = {
            "status": True,
            "result": _("Login succeed!")
        }
        return JsonResponse(result)
    result = {
        "status": False,
        "result": _("Login Failed!")
    }
    return JsonResponse(result)


@check_params(["username", "nickname", "password", "university", "email"])
def register(request):
    # Actually `username` can represent nickname and email
    username = str(request.POST['username'])
    nickname = str(request.POST['nickname'])
    password = str(request.POST['password'])
    score = 0
    university = str(request.POST['university'])
    email = str(request.POST['email'])
    register_ip = str(request.META['REMOTE_ADDR'])  # Get User IP Adderss
    active_code = generate_active_code()  # Generate A Random String
    destroyed = False
    blocked = False
    is_active = False

    # Valid Data
    if len(nickname) > 0x20:
        result = {
            "status": False,
            "result": _("Nickname max length is 32!")
        }
        return JsonResponse(result)

    if len(username) > 0x20:
        result = {
            "status": False,
            "result": _("Username max length is 32!")
        }
        return JsonResponse(result)

    try:
        validate_email(email)
    except ValidationError as e:
        result = {
            "status": False,
            "result": str(e)
        }
        return JsonResponse(result)

    if len(university) > 0x20:
        result = {
            "status": False,
            "result": _("University max length is 32!")
        }
        return JsonResponse(result)

    if len(password) > 0x20 or len(password) < 6:
        result = {
            "status": False,
            "result": _("Password length must between 6 and 32!")
        }
        return JsonResponse(result)

    # Username repeat is not allowed
    user_repeat = User.objects.filter(username__exact=username)
    if user_repeat:
        result = {
            "status": False,
            "result": _("Username has been used!")
        }
        return JsonResponse(result)

    # Email repeat is not allowed
    user_repeat = User.objects.filter(email__iexact=email)
    if user_repeat:
        result = {
            "status": False,
            "result": _("Email has been used!")
        }
        return JsonResponse(result)

    try:
        user = User.objects.create(
            username=username,
            nickname=nickname,
            password=make_password(password),
            university=university,
            email=email,
            score=score,
            register_ip=register_ip,
            active_code=active_code,
            destroyed=blocked,
            blocked=blocked,
            is_active=is_active,
        )
        user.save()
    except ValidationError as e:
        result = {
            "status": True,
            "result": str(e)
        }
        return JsonResponse(result)

    # Generate Response
    result = {
        "status": True,
        "result": _("Register succeed!")
    }

    # Return
    return JsonResponse(result)
