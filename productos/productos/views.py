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
        return HttpResponse("successfully created producto")