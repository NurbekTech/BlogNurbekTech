from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

menu = ['Главная страница', 'Блог', 'Проекта']
def index(request):
    return render(request, 'blog/index.html',{'title': 'Главная страница', 'menu': menu})

def about(request):
    return render(request, 'blog/about.html', {'title': 'О сайте', 'menu': menu})

def category(request):
    return HttpResponse('<h1>Category</h1>')

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Upps</h1>')