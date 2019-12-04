from django.contrib.sites import requests

from .models import Venta
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse
from django.http import JsonResponse
import json

def VentaList(request):
    queryset = Venta.objects.all()
    context = list(queryset.values('id', 'referencia', 'cantidad'))
    return JsonResponse(context, safe=False)

def VentaCreate(request):

    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        venta = Venta()
        venta.referencia = data_json["referencia"]
        venta.cantidad = data_json["cantidad"]
        venta.save()
        requests.post(url='actualizarInventario', json=data_json)
        return HttpResponse("successfully created variable")