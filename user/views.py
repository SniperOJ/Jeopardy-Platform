from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def login(request):
    status = True
    response = {
        'status': status,
        'result': []
    }
    return JsonResponse(response)


def register(request):
    status = True
    response = {
        'status': status,
        'result': []
    }
    return JsonResponse(response)
