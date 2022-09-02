from django.shortcuts import render
#from .models import Evento
#from django.http.response import Http404

def eventos(request):
    return render(request, 'eventos.html', {})

def index (request):
    return render(request, 'index.html', {})

def nosotros (request):
    return render(request, 'nosotros.html', {})

def noticias (request):
    return render(request, 'noticias.html', {})

def registrarme(request):
    return render(request, 'registrame.html', {})

def iniciar_sesion(request):
    return render(request, 'iniciar_sesion.html', {})