from django.contrib import admin
from django.urls import path
from mascotas.views import inicio, mascotas, postular, registro ,login_view, editarPerfil, acerca_de_mi
from django.contrib.auth.views import LogoutView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', inicio, name='inicio'),
    path('mascotas', mascotas, name='mascotas'),
    path('postular', postular.as_view(), name='postular'),
    path('login', login_view, name='login'),
    path('registro', registro, name='registro'),
    path('logout', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('editarperfil', editarPerfil, name='editarperfil'),
    path('sobre_mi', acerca_de_mi, name="sobre_mi")

]