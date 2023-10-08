from django.shortcuts import render, redirect
from bodega.forms import LoginForm, RegistrarUsuarioForm    
from django.contrib.auth import login, logout, authenticate
from bodega.models import PerfilUsuario
# Create your views here.


def index(request):
    
    return render(request, "index.html", {})


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