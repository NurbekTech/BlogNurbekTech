from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
menu = ['Блог', 'Проекты', 'Контакты']


def index(request):
    data = {
        'title': 'Main page',
        'menu': menu
    }
    return render(request, 'blog/index.html', context=data)


def about(request):
    return render(request, 'blog/about.html')
