from django.db import models
from django.contrib.auth.models import User

class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=80, blank=True, null=True, verbose_name="Rut")
    direccion = models.CharField(max_length=80, blank=True, null=True, verbose_name="Dirección")

    def __str__(self):
        return f"{self.user.username} - {self.user.first_name} {self.user.last_name} ({self.user.email})"
    

class Productos (models.Model):
    codigo = models.CharField(primary_key= True, max_length=6)
    nombre = models.CharField(max_length=50)  
    precio = models.IntegerField(int)  
#     Imagen = models.ImageField(upload_to='C:\Projectos_DJANGO\Proyecto-semestral\allYouEat\static\img')

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format (self.nombre, self.precio)
