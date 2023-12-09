from django.shortcuts import render, redirect, get_object_or_404
from bodega.models import Productos, Factura
from django.db.models import F, ExpressionWrapper, DecimalField, Sum, Count
from django.http import HttpResponseServerError
from datetime import datetime
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


# Reporte de facturas


def reporte_facturas(request):
    try:
        if request.method == 'POST':
            fecha_inicio_str = request.POST.get('fecha_inicio')
            fecha_fin_str = request.POST.get('fecha_fin')

            fecha_inicio = datetime.strptime(fecha_inicio_str, '%Y-%m-%d').date()
            fecha_fin = datetime.strptime(fecha_fin_str, '%Y-%m-%d').date()

            facturas = Factura.objects.filter(fecha_factura__range=[fecha_inicio, fecha_fin])

            if not facturas:
                # Manejar el caso en el que no hay facturas en el rango de fechas
                return render(request, 'sin_facturas.html')

            context = {'facturas': facturas, 'fecha_inicio': fecha_inicio, 'fecha_fin': fecha_fin}
            return render(request, 'reporte_facturas.html', context)

    except Exception as e:
        # Manejar otros posibles errores
        return HttpResponseServerError(f'Error: {e}')

    return render(request, 'formulario_fechas.html')
# def reporte_facturas(request):
    
#     if request.method == 'POST':
#         fecha_inicio = request.POST.get('fecha_inicio')
#         fecha_fin = request.POST.get('fecha_fin')

#         facturas = Factura.objects.filter(fecha__range=[fecha_inicio, fecha_fin])

#         # Puedes procesar los datos de ventas como desees y pasarlos al contexto
#         context = {'facturas': facturas, 'fecha_inicio': fecha_inicio, 'fecha_fin': fecha_fin}
#         return render(request, 'reporte_facturas.html', context)

#     return render(request, 'formulario_fechas.html')