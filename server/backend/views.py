from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def index(request):
    obj = {
        'Hackathon': 'DBMS',
        'Team Name': 'IIIT-Nagpur'
    }
    return JsonResponse(obj, safe=False)



def town(request):
    return HttpResponse("DBMS Project 2022")


def Hello(request):
    return HttpResponse("Hi")


def edit(request):
    return HttpResponse("ok done")
