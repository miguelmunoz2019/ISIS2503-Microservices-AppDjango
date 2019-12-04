from django.urls import path
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url('inventarios/', views.InventarioList),
    url('inventariocreate/', csrf_exempt(views.InventarioCreate), name='inventarioCreate'),
]