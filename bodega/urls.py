
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [


    path('', views.mantenedor, name="productos"),
    path('registrarproducto/', views.registrarproducto, name='registrarproducto'),
    path('eliminarProducto/<codigo>', views.eliminarProducto),
    path('edicionProducto/<codigo>', views.edicionProducto),
    path('editarProducto/', views.editarProducto, name='editarProducto'),
    path('orden_de_compra/', views.orden_de_compra, name='orden_de_compra'),
    path('formulario_fechas/', views.reporte_facturas, name='reporte'),
    path('reporte_factura/', views.reporte_facturas, name='detalle_reporte'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
