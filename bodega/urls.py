
from django.urls import path
from . import views


urlpatterns = [


    path('', views.mantenedor, name="productos"),
    path('registrarproducto/', views.registrarproducto, name='registrarproducto'),
    path('eliminarProducto/<codigo>', views.eliminarProducto),
    path('edicionProducto/<codigo>', views.edicionProducto),
    path('editarProducto/', views.editarProducto, name='editarProducto')
]
