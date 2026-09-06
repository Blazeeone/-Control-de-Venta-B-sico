from django.db import models

# Create your models here.  
class Producto(models.Model):
    codigo = models.CharField(max_length=20) # Requerimiento del Caso 2
    nombre = models.CharField(max_length=64)
    precio = models.IntegerField(default=0)
    stock = models.IntegerField(default=0) 

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    rut = models.CharField(max_length=12)
    habitual = models.BooleanField(default=False)
    nombre = models.CharField(max_length=64, null=True, blank=True)
    telefono = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.rut