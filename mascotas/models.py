from django.db import models
from django.contrib.auth.models import User

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
    def __str__(self):
        return f"{self.user} - {self.imagen}"


class mascota(models.Model):
    nombre = models.CharField(max_length=30)
    animal = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()
    informacion_adicional = models.CharField(max_length=150, blank=True)
    imagen = models.ImageField(upload_to='mascotas', null=True, blank=True)

    def __str__(self):
        return self.nombre
