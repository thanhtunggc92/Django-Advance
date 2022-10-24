import re
from django.shortcuts import render
from django.http import HttpResponse

def Home(request):
# Create your views here.
    return HttpResponse('Hello work')