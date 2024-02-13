from django.db import models

# Create your models here.

class mascota(models.Model):
    nombre = models.CharField( max_length=15)
    animal = models.CharField(max_length=10)

class adoptante(models.Model):
    nombre = models.CharField(max_length=30)
    mail = models.EmailField()
    
class centro_adopcion(models.Model):
    pais = models.CharField(max_length = 15)
    calle = models.CharField(max_length = 20)
    abierto = models.BooleanField()