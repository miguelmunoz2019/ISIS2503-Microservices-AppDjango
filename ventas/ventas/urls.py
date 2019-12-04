from django.urls import path
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^ventas/', views.VentaList, name='ventaList'),
    url(r'^ventacreate/$', csrf_exempt(views.VentaCreate), name='ventaCreate'),
]