from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=64)
    precio = models.IntegerField(default=0)
    descripcion = models.CharField(max_length=128, null=True, blank=True)
    stock = models.IntegerField(default=0)