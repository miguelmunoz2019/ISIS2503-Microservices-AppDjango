from django.urls import path
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^inventarios/', views.InventarioList),
    url(r'^inventariocreate/$', csrf_exempt(views.InventarioCreate), name='inventarioCreate'),
]