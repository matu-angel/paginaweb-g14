from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})

def nosotros(request):
    return render(request, 'nosotros.html')

def noticias (request):
    return render(request, 'noticias.html', {})

def eventos(request):
    return render(request, 'eventos.html', {})

def recursos(request):
    return render(request, 'recursos.html', {})

#def registrarme(request):
 #   return render(request, 'registrame.html', {})

#def iniciar_sesion(request):
  #  return render(request, 'iniciar_sesion.html', {})
