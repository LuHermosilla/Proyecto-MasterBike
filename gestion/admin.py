from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Clientes)
admin.site.register(Proveedores)
admin.site.register(CategoriaProducto)
admin.site.register(Producto)
admin.site.register(Inventario)
admin.site.register(EstadosPedido)
admin.site.register(Pedidos)
admin.site.register(DetallePedido)
admin.site.register(Ventas)
admin.site.register(Cargos)
admin.site.register(Empleado)
admin.site.register(Sucursales)
admin.site.register(EstadoEnvios)
admin.site.register(Envios)
admin.site.register(InformesGestion)
admin.site.register(EstadosArriendo)
admin.site.register(Arriendos)
admin.site.register(EstadosReparacion)
admin.site.register(Reparaciones)
admin.site.register(HistorialMantenciones)
admin.site.register(Eventos)
admin.site.register(TrazabilidadEnvios)
admin.site.register(TipoPromocion)
admin.site.register(Promociones)
