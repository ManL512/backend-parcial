#api/models.py

from django.db import models

class Articulo(models.Model):
    titulo = models.CharField(max_length=100)
    imagen = models.URLField()
    vendedor = models.CharField(max_length=100)
    calificacion = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo
