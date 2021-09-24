from django.shortcuts import render, get_object_or_404

from .models import Post, Group

# Главная страница
def index(request):
    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию (от больших значений к меньшим)
    title = 'Последние обновления на сайте'
    posts = Post.objects.order_by('-pub_date')[:10]
    # В словаре context отправляем информацию в шаблон
    context = {
        'title': title,
        'posts': posts,
    }
    return render(request, 'posts/index.html', context) 


# Страница с постами сгруппированными по темам
def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group__slug=slug).order_by('-pub_date')[:10]
    # В словаре context отправляем информацию в шаблон
    context = {
        'slug': group.slug,
        'title': group.title,
        'description': group.description,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
