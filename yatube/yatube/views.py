from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    template = 'yatube/index.html'
    return render(request, template) 
