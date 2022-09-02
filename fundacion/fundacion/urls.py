"""fundacion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.urls import re_path as url
from django.contrib import admin
from django.urls import path
#from apps.blog_auth import views as viewsUsers
from apps.noticias_app import views
#from apps.eventos_app import views 
#from django.conf.urls.static import static
#from django.conf import settings
#from django.contrib.auth.views import LoginView,LogoutView
from django.conf.urls import *
admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('noticias/', views.noticias, name='noticias'),
    path('eventos/', views.eventos, name='eventos'),
    path('recursos/', views.recursos, name='recursos'),
    #path("registrame/", views.formulario, name="registrarme"),
    #path('iniciar_sesion/', views.noticias, name='iniciar_sesion'),

] 
#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT, show_indexes=True) 