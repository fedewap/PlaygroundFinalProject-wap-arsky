from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import registroform, UserEditForm, form_mascota
from django.contrib.auth.views import LogoutView
from mascotas import forms, models
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import mascota
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View




def acerca_de_mi(request):
    return render(request, 'acerca_de_mi.html')

def inicio(request):
    return render(request, 'index.html')

def mascotas(request):
    mascotas_postuladas = mascota.objects.all()
    return render(request, 'mascotas.html', {'mascotas': mascotas_postuladas})

class postular(LoginRequiredMixin, View):
    def get(self, request):
        form = form_mascota()
        return render(request, 'postular.html', {'form': form})

    def post(self, request):
        form = form_mascota(request.POST, request.FILES)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            animal = form.cleaned_data['animal']
            fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
            informacion_adicional = form.cleaned_data.get('informacion_adicional', '')
            imagen = form.cleaned_data.get('imagen', None)

            nueva_mascota = mascota(
                nombre=nombre,
                animal=animal,
                fecha_nacimiento=fecha_nacimiento,
                informacion_adicional=informacion_adicional,
                imagen=imagen
            )
            nueva_mascota.save()
            return redirect(reverse('mascotas'))
        return render(request, 'postular.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')
            user = authenticate( username=usuario, password=contraseña)
            
            login(request, user)
            return render(request, 'index.html')
        else:
            return render(request, 'login.html', {"mensaje": 'no se ha podido iniciar sesion, prueba con otros datos' })
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {"form":form})

def logout(request):
    return LogoutView.as_view()(request)

def registro(request):
    if request.method == 'POST':
        form = registroform(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            form.save()
            return render(request, 'index.html')
        else:
            return render(request, 'registro.html', {"form":form})
    else:
        form = registroform()
        return render(request, "registro.html", {"form":form})

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        miFormulario = forms.UserEditForm(request.POST, request.FILES, instance=request.user)
        if miFormulario.is_valid():
            if miFormulario.cleaned_data.get('imagen'):
                if hasattr(usuario, 'avatar'):
                    usuario.avatar.imagen = miFormulario.cleaned_data.get('imagen')
                    usuario.avatar.save()
                else:
                    models.Avatar.objects.create(user=usuario, imagen=miFormulario.cleaned_data.get('imagen'))
            miFormulario.save()
            return render(request, "index.html")
    else:
        miFormulario = forms.UserEditForm(instance=request.user)
    return render(request, "edicion_usuario.html", {"miFormulario": miFormulario, "usuario": usuario})