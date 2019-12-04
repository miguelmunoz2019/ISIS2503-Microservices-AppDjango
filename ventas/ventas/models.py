from django.db import models

class Venta(models.Model):
    referencia = models.FloatField(null=True, blank=True, default=None)
    cantidad = models.FloatField(null=True, blank=True, default=None)

    def __str__(self):
        return '{}'.format(self.referencia)