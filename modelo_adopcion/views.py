from django.shortcuts import render
from django.http import HttpResponse
from modelo_adopcion.forms import form_mascota, form_centro, form_adoptante
from modelo_adopcion.models import mascota, adoptante, centro_adopcion
from modelo_adopcion import models

# Create your views here.
def inicio(request):
    return render(request, 'modelo_clientes\inicio.html')

def adoptante(request):
    return render(request, 'modelo_clientes\\adoptante.html')

def centro_adopcion(request):
    return render(request, 'modelo_clientes\\centro_adopcion.html')




def formulario_mascotas(request):
    if request.method == 'POST':
        form = form_mascota(request.POST) 
        
        print(form)
        
        if form.is_valid:
            info = form.cleaned_data
            nueva_mascota = mascota(nombre=info["nombre"], animal=info["animal"])
            nueva_mascota.save()
            return render(request, 'modelo_clientes/inicio.html')
    else:
        form = form_mascota() 

    return render(request, 'modelo_clientes/mascota.html', {'form': form})

def formulario_adoptante(request):
    if request.method == 'POST':
        form = form_adoptante(request.POST) 
        
        print(form)
        
        if form.is_valid:
            info = form.cleaned_data
            nuevo_adoptante = adoptante(nombre=info["nombre"], mail=info["mail"])
            nuevo_adoptante.save()
            return render(request, 'modelo_clientes/inicio.html')
    else:
        form = form_adoptante() 

    return render(request, 'modelo_clientes/adoptante.html', {'form': form})

def formulario_centro(request):
    if request.method == 'POST':
        form = form_centro(request.POST) 
        print(form)
        if form.is_valid:
            info = form.cleaned_data
            nuevo_centro = centro_adopcion(pais=info["pais"], calle=info["calle"], abierto=info['abierto'])
            nuevo_centro.save()
            return render(request, 'modelo_clientes/inicio.html')
    else:
        form = form_centro() 

    return render(request, 'modelo_clientes/centro_adopcion.html', {'form': form})

#def buscar(request):
 #   if request.GET["nombre"]:
  #      nombre = request.GET["nombre"]
   #     mascotas = models.mascota.objet.filter(nombre_iconteins=nombre)
    #    return render(request, 'modelo_clientes\buscar.html', {'mascotas' : mascotas , 'nombre':nombre})
    #else:
     #   respuesta="no enviaste datos"
    #return render(request, 'modelo_clientes\buscar.html', {'respuesta':respuesta})

def buscar(request):
    respuesta = ""  # Inicializa la variable respuesta fuera del condicional
    
    if 'nombre' in request.GET:
        nombre = request.GET['nombre']
        mascotas = models.mascota.objects.filter(nombre__icontains=nombre)  # Corrige el nombre del modelo y el método filter
        return render(request, 'modelo_clientes/buscar.html', {'mascotas': mascotas, 'nombre': nombre})
    else:
        respuesta = "No enviaste datos"
    
    return render(request, 'modelo_clientes/buscar.html', {'respuesta': respuesta})
