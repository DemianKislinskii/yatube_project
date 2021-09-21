from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# Главная страница
def index(request):
    template = 'posts/index.html'
    title = 'Последние обновления на сайте'
    text = 'Это главная страница проекта Yatube'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, template, context) 


# Страница с постами сгруппированными по темам
def group_posts(request, slug):
    template = 'posts/group_list.html'
    title = 'Записи сообщества'
    text = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, template, context)
