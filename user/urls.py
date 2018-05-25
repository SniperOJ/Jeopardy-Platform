#!/usr/bin/env python
#  -*- coding: utf-8 -*-

from django.urls import path

from .views import login
from .views import register

urlpatterns = [
    path('login', login),
    path('register', register),
    # path('active', register),
    # path('reset', register),
    # path('destroy', register),
]
