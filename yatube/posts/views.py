from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница социальной сети Yatube')


def group_posts(request, slug):
    return HttpResponse(f'Страница сообщества {slug}')