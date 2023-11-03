from django.contrib import admin
from .models import Productos, Factura, PerfilUsuario
# Register your models here.

admin.site.register(Productos)
admin.site.register(Factura)
admin.site.register(PerfilUsuario)