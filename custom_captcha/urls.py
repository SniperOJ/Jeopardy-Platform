#!/usr/bin/env python
#  -*- coding: utf-8 -*-

from django.urls import path
from .views import *

urlpatterns = [
    path('generate', generate_captcha),
    path('validate', validate_captcha),
]
