from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def list_all(request):
    status = True
    response = {
        'status': status,
        'result': []
    }
    return JsonResponse(response)
