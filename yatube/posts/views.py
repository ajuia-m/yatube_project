from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse('She was fokin crazy')

def group_posts(request, pk):
    return HttpResponse(f'She was insane {pk}')