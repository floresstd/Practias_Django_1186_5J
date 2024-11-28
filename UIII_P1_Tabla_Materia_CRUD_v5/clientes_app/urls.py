from django.urls import path
from clientes_app import views
urlpatterns = [
    path('cliente', views.inicio_vistaCliente, name="inicio_vistaCliente")
    
]
