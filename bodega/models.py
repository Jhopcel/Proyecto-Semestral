from django.db import models
from django.contrib.auth.models import User

class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=80, blank=True, null=True, verbose_name="Rut")
    direccion = models.CharField(max_length=80, blank=True, null=True, verbose_name="Dirección")
    telefono = models.CharField(max_length=19, default="NO Ingresado",blank=True, null=True)
    comuna = models.CharField(max_length=100, default="No Ingresado", blank=True, null=True)
    region = models.CharField(max_length=100, default="No Ingresado", blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.user.first_name} {self.user.last_name} ({self.user.email})"
    

class Productos (models.Model):
    codigo = models.CharField(primary_key= True, max_length=6)
    nombre = models.CharField(max_length=50)  
    precio = models.IntegerField(int)  
    imagen = models.ImageField(upload_to='images/', default="sinfoto.jpg")

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format (self.nombre, self.precio)

class Factura(models.Model):
    codigo_factura = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE)
    nombre_producto = models.CharField(max_length=90, null=True)
    monto_producto = models.IntegerField(default=1, blank=True, null=True)
    precio_producto = models.IntegerField()
    fecha_factura = models.DateTimeField(auto_now=True)
    estado_factura = models.CharField(max_length=40 ,default="Pendiente", null=True, blank=True)