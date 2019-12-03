from django.db import models
from django.forms import IntegerField


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    id = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    carrito = models.ManyToManyField(IntegerField(null=False))

    def __str__(self):
        return '%s %s' % (self.value, self.unit)
