from .models import Producto
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse
from django.http import JsonResponse
import json


def ProductoList(request):
    queryset = Producto.objects.all()
    context = list(queryset.values('id', 'nombre', 'marca', 'precio', 'talla', 'cantidad', 'descripcion'))
    return JsonResponse(context, safe=False)


def ProductoCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        producto = Producto()
        producto.id = data_json["id"]
        producto.nombre = data_json["nombre"]
        producto.marca = data_json["marca"]
        producto.precio = data_json["precio"]
        producto.talla = data_json["talla"]
        producto.cantidad = data_json["cantidad"]
        producto.descripcion = data_json["descripcion"]
        producto.save()
        return HttpResponse("successfully created producto")