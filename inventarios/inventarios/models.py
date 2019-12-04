from django.db import models

class Inventario(models.Model):
    referencia = models.FloatField(primary_key=True, default=None)
    cantidad = models.FloatField(null=True, blank=True, default=None)

    def __str__(self):
        return '%s %s' % (self.value, self.unit)