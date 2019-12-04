from .models import Cliente
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
    r = requests.get(settings.PATH_VAR, headers={"Accept": "application/json"})
    productos = r.json()
    cadena= data["carrito"].split(',')
    for producto in productos:
        for numero in cadena:
            if numero == producto["id"]:
                return True
    return False


def cliente_list(request):
    queryset = Cliente.objects.all()
    context = list(queryset.values('nombre', 'id', 'direccion', 'correo', 'carrito'))
    return JsonResponse(context, safe=False)


def ClienteCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        cliente = Cliente()
        if check_producto(data_json):
            cliente.id = data_json['id']
            cliente.nombre = data_json['nombre']
            cliente.direccion = data_json['direccion']
            cliente.correo = data_json['correo']
            cliente.carrito = data_json['carrito']
            cliente.save()
            return HttpResponse("successfully added producto to carrito")
        return HttpResponse("ERROR")
