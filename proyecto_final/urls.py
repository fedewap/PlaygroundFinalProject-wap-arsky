"""
URL configuration for proyecto_final project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from mascotas.views import inicio, mascotas, postular, registro ,login, editarPerfil
from django.contrib.auth.views import LogoutView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('miapp/', include('mascotas.urls')),
    path('', inicio, name='inicio'),
  #  path('mascotas', mascotas, name='mascotas'),
   # path('postular', postular, name='postular'),
    #path('login', login, name='login'),
    #path('registro', registro, name='registro'),
    #path('logout', LogoutView.as_view(template_name='logout.html'), name='logout'),
    #path('editarperfil', editarPerfil, name='editarperfil')

]


urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)