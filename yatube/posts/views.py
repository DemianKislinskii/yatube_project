from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# Главная страница
def index(request):
    template = 'posts/index.html'
    return render(request, template) 


# Страница с постами сгруппированными по темам
def group_posts(request, slug):
    template = 'posts/group_list.html'
    return render(request, template)
