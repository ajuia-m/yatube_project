from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request, slug):
    return HttpResponse(f'She was insane {slug}')