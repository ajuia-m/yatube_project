from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    template = 'index.html'
    return render(request, template) 


def group_posts(request, slug):
    return HttpResponse(f'She was insane {slug}')