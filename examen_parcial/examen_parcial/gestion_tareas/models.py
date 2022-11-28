from django.db import models

# Se confuguran las classes en models 
class usuario(models.Model):
    nombre = models.CharField(max_length=64, default='')
    apellido = models.CharField(max_length=64, default='')
    codigo = models.CharField(max_length=64, default='')
    clave = models.CharField(max_length=64, default='')

class tarea(models.Model):
    titulo = models.CharField(max_length=64, default='')
    descripcion = models.CharField(max_length=64, default='')
    date_creation = models.CharField(max_length=64, default='')
    date_entrega = models.CharField(max_length=64, default='')
    usuario = models.CharField(max_length=64, default='')