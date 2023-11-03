from django.shortcuts import render, redirect
from bodega.models import Productos

# Create your views here.


def mantenedor(request):
    productosListados = Productos.objects.all()
    return render(request, "Productos.html", {"productos": productosListados})

def registrarproducto(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    precio = request.POST['intPrecio']
    imagen = request.FILES['imgProducto']
    
    producto = Productos.objects.create(codigo=codigo, nombre=nombre, precio=precio, imagen = imagen)
    return redirect('/')

def eliminarProducto(request, codigo):
    producto = Productos.objects.get(codigo=codigo)
    producto.delete()
    return redirect('/')

def edicionProducto(request, codigo):
    producto = Productos.objects.get(codigo=codigo)
    return render(request, "edicionProducto.html", {"producto": producto})


def editarProducto(request):
    
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    precio = request.POST['intPrecio']
    imagen = request.FILES['imgProducto']
    
    producto = Productos.objects.get(codigo=codigo)
    producto.nombre = nombre
    producto.precio = precio
    producto.imagen = imagen
    producto.save()

    return redirect('/')