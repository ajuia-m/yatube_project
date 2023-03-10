from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post, Group

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
    posts = Post.objects.order_by('-group')[:10]
    context = {
        'text':"Здесь будет информация о группах проекта Yatube",
        'posts': posts,
        }
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context) 