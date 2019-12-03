from django.urls import path
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views


urlpatterns = [
    path(r'^productos/', views.ProductoList),
    path(r'^productocreate/$', csrf_exempt(views.ProductoCreate), name='productoCreate'),
]
