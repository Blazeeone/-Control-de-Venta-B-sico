from django.db import models

class Producto(models.Model):
    codigo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=64)
    # PositiveIntegerField bloquea los números negativos desde la base de datos
    precio = models.PositiveIntegerField(default=1)
    stock = models.PositiveIntegerField(default=0) 

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    rut = models.CharField(max_length=12)
    habitual = models.BooleanField(default=False)
    nombre = models.CharField(max_length=64, null=True, blank=True)
    telefono = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.rut