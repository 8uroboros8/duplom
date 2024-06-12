from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
def index(request):
    return HttpResponse('Працює')

def games(request, gameid):
    if gameid > 4:
        return redirect('home', permanent=False)
    return HttpResponse(f'<h1>Ігри</h1><p>{gameid}</p>')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Сторінку не знайдено</h1>')