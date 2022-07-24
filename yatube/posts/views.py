from re import template
from django.shortcuts import get_object_or_404, render
# Импортируем модель, чтобы обратиться к ней
from .models import Group, Post
from typing import Dict


def index(request):
    template: str = 'posts/index.html'
    posts = Post.objects.order_by('-pub_date')[:10]
    context: Dict[str, str] = {
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    template: str = 'posts/group_list.html'
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context: Dict[str, str] = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)