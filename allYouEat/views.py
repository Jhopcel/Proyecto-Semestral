from django.shortcuts import render, redirect
from bodega.forms import LoginForm, RegistrarUsuarioForm    
from django.contrib.auth import login, logout, authenticate
from bodega.models import PerfilUsuario, Productos, Factura
from django.contrib import messages

# linea para el mantenedor
from django.urls import path
from bodega import views
# Create your views here.


def index(request):
    productos = Productos.objects.all()
    return render(request, "index.html", {'productos': productos})

def producto(request, id):
    producto = Productos.objects.filter(codigo=id)

    producto_valores = Productos.objects.get(codigo=id)
    
    if request.method == 'POST':
        if request.user.is_authenticated:
            if not request.user.is_staff:
                user = request.user
                perfil = PerfilUsuario.objects.get(user=user)
                usuario = perfil
                nombre_producto = producto_valores.nombre
                precio_producto = producto_valores.precio     
                factura = Factura.objects.create(usuario=usuario, nombre_producto=nombre_producto, precio_producto=precio_producto)
                
                messages.success(request, "Se puedo comprar exitosamente")
                return redirect("factura", id=factura.pk)
            else:
                messages.error(request, "Un administrador no puede comprar")
        else:
            messages.error(request, "Tienes que tener una cuenta para poder comprar")
    return render(request, "producto.html", {'productos': producto})

def perfil_usuario(request):
    
    usuario = request.user
    
    perfil = PerfilUsuario.objects.get(user=usuario)
    facturas = Factura.objects.filter(usuario=perfil)
    
    return render(request, "perfil_usuario.html", {'perfil':perfil, 'facturas': facturas})

def factura(request, id):
    factura = Factura.objects.filter(codigo_factura = id)
    return render(request, "factura.html", {'factura': factura})

def login_succes(request):
    data = {"mesg": "", "form": LoginForm()}

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid:
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(to='index')
                else:
                    data["mesg"] = "¡Nombre de usuario o contraseña no son correctos!"
            else:
                data["mesg"] = "¡Nombre de usuario o contraseña no son correctos!"
    return render(request, 'login.html', data)

def logout_succes(request):
    logout(request)
    # Redirige al usuario a la página de inicio de sesión o a cualquier otra página que desees.
    return redirect('index')

def registro(request):
    if request.method == 'POST':
        form = RegistrarUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            rut = request.POST.get("rut")
            direccion = request.POST.get("direccion")
            PerfilUsuario.objects.update_or_create(user=user, rut=rut, direccion=direccion)
            return redirect(login_succes) 
    form = RegistrarUsuarioForm()
    return render(request, "registro.html", context={'form': form})

def orden_de_compra(request):
    
    return render(request, "orden_de_compra.html", {})
# conexion a mantenedor
urlpatterns = [

    path('Productos.html', views.mantenedor),
    path('editarProducto/', views.editarProducto)
    
]
