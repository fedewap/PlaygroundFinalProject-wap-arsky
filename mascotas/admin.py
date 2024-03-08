from django.contrib import admin
from mascotas import models
from .models import mascota

admin.site.register(models.Avatar)
# Register your models here.

admin.site.register(mascota)
