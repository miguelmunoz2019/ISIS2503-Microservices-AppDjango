from django.db import models


class ProductoCarrito(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    id = models.IntegerField(primary_key=True)
    direccion = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    carrito = models.ManyToManyField(ProductoCarrito)


    def __str__(self):
        return '%s %s' % (self.value, self.unit)
