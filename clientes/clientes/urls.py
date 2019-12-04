from django.urls import path
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views


urlpatterns = [
    path('clientes/', views.cliente_list),
    path('clientecreate/', csrf_exempt(views.ClienteCreate), name='clienteCreate'),
    path('clienteadd/', csrf_exempt(views.AddProductoCarro), name='AddProductoCarro'),
]

