from .models import Inventario
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from django.conf import settings
import requests
import json

def check_venta(data):
    r = requests.get(settings.PATH_VAR, headers={"Accept":"application/json"})
    ventas = r.json()
    for venta in ventas:
        if data["venta"] == venta["id"]:
            return True
    return False

def InventarioList(request):
    queryset = Inventario.objects.all()
    context = list(queryset.values('id', 'referencia', 'cantidad'))
    return JsonResponse(context, safe=False)

def InventarioCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        inventario = Inventario()
        inventario.referencia = data_json['referencia']
        inventario.cantidad = data_json['cantidad']
        inventario.save()
        return HttpResponse("successfully created measurement")

def InventarioActualizar(request):
    if request.method == 'PUT':
       data = requests.get(url= 'ventaCreate')
       data_json= json.load(data)
       inventario =  Inventario()
       inventario.referencia= data_json['referencia']
       inventario.cantidad= inventario.cantidad - data_json['cantidad']