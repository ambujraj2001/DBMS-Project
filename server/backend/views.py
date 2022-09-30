from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def index(request):
    obj = {
        'Hackathon': 'SIH-2022',
        'Team Name': 'Access Denieded'
    }
    return JsonResponse(obj, safe=False)


def home(request):
    return HttpResponse("SIH-2022 App")
