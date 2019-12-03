from .models import Cliente
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from django.conf import settings
import requests
import json

def check_producto(data):
    r = requests.get(settings.PATH_VAR, headers={"Accept":"application/json"})
    productos = r.json()
    for producto in productos:
        if data["producto"] == producto["id"]:
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
        if check_producto(data_json) == True:
            cliente = Cliente()
            cliente.nombre = data_json['nombre']
            cliente.id = data_json['id']
            cliente.direccion = data_json['direccion']
            cliente.correo = data_json['correo']
            cliente.carrito = data_json['carrito']
            producto.save()
            return HttpResponse("successfully created cliente")
        else:
            return HttpResponse("unsuccessfully created cliente. producto does not exist")
