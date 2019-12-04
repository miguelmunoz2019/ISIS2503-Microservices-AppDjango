from .models import Cliente,ProductoCarrito
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from django.conf import settings
from django.db import connection
import requests
import json


def check_producto(data):
    r = requests.get(settings.PATH_VAR, headers={"Accept":"application/json"})
    productos = r.json()
    for producto in productos:
        if data["nombre"] == producto["id"]:
            return True
    return False


def cliente_list(request):
    queryset = Cliente.objects.all()
    context = list(queryset.values('nombre', 'id', 'direccion', 'correo' ))
    return JsonResponse(context, safe=False)


def ClienteCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)

        cliente = Cliente()
        cliente.id = data_json['id']
        cliente.nombre = data_json['nombre']
        cliente.direccion = data_json['direccion']
        cliente.correo = data_json['correo']

        cliente.save()
        return HttpResponse("successfully created cliente")


def AddProductoCarro(request):
    if request.method == 'PUT':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)

        if check_producto(data_json):
            cliente = data_json['id']
            producto = ProductoCarrito()
            producto.id = data_json['nombre']
            updateSQL(cliente, producto)
        return HttpResponse("successfully created cliente")


def updateSQL(id,producto):
    for p in Cliente.objects.raw('SELECT * FROM '+ 'clientes_Cliente '+ 'WHERE id ='+ str(id)):
        p.carrito.add(producto)
        p.save()


