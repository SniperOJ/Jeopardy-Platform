#!/usr/bin/env python
#  -*- coding: utf-8 -*-

# from django.urls import path
#
# from .views import generate
# from .views import validate
#
# urlpatterns = [
#     path('generate/', generate),
#     path('validate/', validate),
#
# ]

from django.urls import path
from .views import *

urlpatterns = [
    path('generate/', generate_captcha),
    path('validate/', validate_captcha),
]
