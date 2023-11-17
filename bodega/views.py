from django.shortcuts import render, redirect, get_object_or_404
from bodega.models import Productos, Factura
from django.db.models import F, ExpressionWrapper, DecimalField, Sum, Count
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

def orden_de_compra(request):
    factura = Factura.objects.all()
    
    if request.method == "POST":
        valor_id = request.POST['factura_id']
        factura_cambio = request.POST['estado']
        
        obtener_factura = get_object_or_404(Factura, pk=valor_id)
        obtener_factura.estado_factura = factura_cambio
        
        obtener_factura.save()
    return render(request, "orden_de_compra.html", {'factura':factura})