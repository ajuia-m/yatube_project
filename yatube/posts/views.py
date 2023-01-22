from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    template = 'posts/index.html'
    context = {
        'text':"Это главная страница проекта Yatube",
        'posts': posts,
        }
    return render(request, template, context) 

def group_list(request):
    template = 'posts/group_list.html'
    context = {'text':"Здесь будет информация о группах проекта Yatube"}
    return render(request, template, context)


def group_posts(request, slug):
    return HttpResponse(f'She was insane {slug}')