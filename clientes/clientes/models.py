from django.db import models



class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    id = models.IntegerField(primary_key=True)
    direccion = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    carrito = models.CharField(max_length=50)


    def __str__(self):
        return '%s %s' % (self.value, self.unit)
