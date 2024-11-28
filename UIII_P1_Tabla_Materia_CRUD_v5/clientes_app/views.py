from django.shortcuts import render,redirect
from .models import Cliente
# Create your views here.

def inicio_vistaCliente(request):
    losclientes = Cliente.objects.all()
    return render(request, "gestionarClientes.html", {"misclientes":losclientes})
def registrarCliente(request):
    nombre = request.POST["txtnombre"]
    telefono = request.POST["txttelefono"]
    email = request.POST["txtemail"]
    direccion = request.POST["txtdireccion"]

    guardarcliente = Cliente.objects.create(
        Nombre=nombre, Telefono=telefono, Email=email, Direccion=direccion
    )  # GUARDA EL REGISTRO

    return redirect("/")

def seleccionarCliente(request, id_cliente):
    cliente = Cliente.objects.get(id_Cliente=id_cliente)
    return render(request, "editarcliente.html", {"misclientes": cliente})

def editarCliente(request):
    id_cliente = request.POST["txtid_cliente"]
    nombre = request.POST["txtnombre"]
    telefono = request.POST["txttelefono"]
    email = request.POST["txtemail"]
    direccion = request.POST["txtdireccion"]
    cliente = Cliente.objects.get(id_Cliente=id_cliente)
    cliente.Nombre = nombre
    cliente.Telefono = telefono
    cliente.Email = email
    cliente.Direccion = direccion
    cliente.save()  # guarda el registro actualizado
    return redirect("/")

def borrarCliente(request, id_cliente):
    cliente = Cliente.objects.get(ID_Cliente=id_cliente)
    cliente.delete()  # borra el registro
    return redirect("/")