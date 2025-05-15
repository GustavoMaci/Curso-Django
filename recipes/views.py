from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'recipes/home.html')

def contato(request):
    return HttpResponse('<h1>contato</h1>')

def sobre(request):
    return HttpResponse('<h1>sobre</h1>')

