from django.contrib import admin
from modelo_adopcion import models

admin.site.register(models.mascota)
admin.site.register(models.adoptante)
admin.site.register(models.centro_adopcion)
