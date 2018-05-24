from django.urls import path

from .views import login
from .views import register


urlpatterns = [
    path('login/', login),
    path('register/', register),
]