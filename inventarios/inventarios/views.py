from .models import Inventario
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse
from django.http import JsonResponse
import json



def InventarioList(request):
    queryset = Inventario.objects.all()
    context = list(queryset.values('referencia', 'cantidad'))
    return JsonResponse(context, safe=False)

def InventarioCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        inventario = Inventario()
        inventario.referencia = data_json['referencia']
        inventario.cantidad = data_json['cantidad']
        inventario.save()
        return HttpResponse("successfully added to inventario ")
