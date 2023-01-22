from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.

# Главная страница
def index(request):    
    template = loader.get_template('ice_cream/index.html')  
    return HttpResponse(template.render({}, request))  

# Страница со списком мороженого
def ice_cream_list(request):
    return HttpResponse('Список мороженого')


# Страница с информацией об одном сорте мороженого;
# view-функция принимает параметр pk из path()
def ice_cream_detail(request, slug):
    return HttpResponse(f'Мороженое номер {slug}') 