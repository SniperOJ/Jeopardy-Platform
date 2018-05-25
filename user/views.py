#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import login as django_login
from django.contrib.auth import authenticate as django_authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# def login(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = django_authenticate(request, username=username, password=password)
#     if user is not None:
#         django_login(request, user)
#         status = True
#         response = {
#             'status': status,
#             'result': []
#         }
#     else:
#         status = False
#         response = {
#             'status': status,
#             'result': []
#         }
#     return JsonResponse(response)

# def register(request):
#     status = True
#     response = {
#         'status': status,
#         'result': []
#     }
#     return JsonResponse(response)

# Import Project lib
from ..utils.session import clear_session
from ..utils.form import check_params

from .models import User

# Import System lib
from datetime import datetime


@clear_session
@check_params(["email", "nickname", "password", "gender", "birthday", "motto"])
def register(request):
    # Get data from POST data
    email = str(request.POST['email']).lower()
    nickname = str(request.POST['nickname'])
    password = str(request.POST['password'])
    gender = str(request.POST['gender'])
    birthday = str(request.POST['birthday'])

    try:
        User.objects.create(
            email=email,
            nickname=nickname,
        )
        result = {
            "status": True,
            "result": "Register succeed!"
        }
        return JsonResponse(result)
    except Exception as e:
        result = {
            "status": False,
            "reason": str(e)
        }
        return JsonResponse(result)
