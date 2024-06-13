from django.db import models

# Create your models here.

class Clientes(models.Model):
    id_cliente = models.IntegerField(primary_key=True),
    nombre_cli = models.CharField(max_length=20),
    aPaterno_cli = models.CharField(max_length=20),
    aMaterno_cli = models.CharField(max_length=20),
    rut = models.CharField(unique=True,blank=False,null=False),
    direccion = models.CharField(max_length=50,blank=True,null=True),
    telefono = models.CharField(max_length=15),
    email = models.EmailField(max_length=100,unique=True),
    fecha_registro = models.DateField(blank=False,null=False),
    clave = models.CharField(max_length=100,blank=False,null=False)
    
class Proveedores(models.Model):
    id_proveedor = models.IntegerField(primary_key=True)
    nombre_prov = models.CharField(max_length=40)
    rut_prov = models.CharField(max_length=20, unique=True)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    email = models.EmailField(max_length=100,unique=True)
    
class CategoriaProductos(models.Model):
    id_categoria = models.IntegerField(primary_key=True)
    nombre_categoria = models.CharField(max_length=20)
    
class Productos(models.Model):
    id_producto = models.IntegerField(primary_key=True),
    nombre_prod = models.CharField(max_length=20),
    categoria = models.ForeignKey('CategoriaProductos',on_delete=models.CASCADE, db_column='id_categoria')
    precio_unit = models.IntegerField(9,2),
    impuesto = models.IntegerField(9,2),
    stock_actual = models.IntegerField(9,2),
    id_proveedor = models.ForeignKey('Proveedores',on_delete=models.CASCADE, db_column='id_proveedor')
    
class Inventario(models.Model):
    id_inventario = models.IntegerField(primary_key=True)
    id_producto = models.ForeignKey('Productos',on_delete=models.CASCADE, db_column='id_producto')
    cantidad = models.IntegerField(9)
    fecha_entrada = models.DateField(blank=False,null=False)

class Sucursales(models.Model):
    id_sucursal = models.IntegerField(primary_key=True)
    nombre_sucursal = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    
class Empleados(models.Model):
    id_empleado = models.IntegerField(primary_key=True)
    nombre_emp = models.CharField(max_length=20)
    aPaterno_emp = models.CharField(max_length=20)
    aMaterno_emp = models.CharField(max_length=20)
    rut_emp = models.CharField(max_length=20, unique=True)
    cargo_emp = models.ForeignKey('Cargos',on_delete=models.CASCADE, db_column='id_cargo')
    id_sucursal = models.ForeignKey('Sucursales',on_delete=models.CASCADE, db_column='id_sucursal')
    
class EstadosPedido(models.Model):
    id_estado = models.IntegerField(primary_key=True)
    estado_pedido = models.CharField(max_length=20)
    
class Pedidos(models.Model):
    id_pedido= models.IntegerField(primary_key=True)
    id_cliente= models.ForeignKey('Clientes',on_delete=models.CASCADE, db_column='id_cliente')
    id_empleado= models.ForeignKey('Empleados',on_delete=models.CASCADE, db_column='id_empleado')
    fecha_pedido= models.DateField(blank=False,null=False)
    estado_pedido= models.ForeignKey('EstadosPedido',on_delete=models.CASCADE, db_column='id_estado')
    
class DetallePedido(models.Model):
    id_detalle = models.IntegerField(primary_key=True)
    id_pedido = models.ForeignKey('Pedidos',on_delete=models.CASCADE, db_column='id_pedido')
    id_producto = models.ForeignKey('Productos',on_delete=models.CASCADE, db_column='id_producto')
    cantidad = models.IntegerField(9)
    precio_unitario = models.IntegerField(9)
    
class Ventas(models.Model):
    id_venta = models.IntegerField(primary_key=True)
    id_pedido = models.ForeignKey('Pedidos',on_delete=models.CASCADE, db_column='id_pedido')
    fecha_venta = models.DateField(blank=False,null=False)
    total_neto = models.IntegerField(9)
    total_impuesto = models.IntegerField(9)
    total_final = models.IntegerField(9)
    
class Cargos(models.Model):
    id_cargo = models.IntegerField(primary_key=True)
    cargo_emp = models.CharField(max_length=20) 
    
class EstadoEnvios(models.Model):
    id_estado_envio = models.IntegerField(primary_key=True)
    estado_envio = models.CharField(max_length=20)
    
class Envios(models.Model):
    id_envio = models.IntegerField(primary_key=True)
    id_venta = models.ForeignKey('Ventas',on_delete=models.CASCADE, db_column='id_venta')
    direccion_envio = models.CharField(max_length=50)
    costo_envio = models.IntegerField(9)
    fecha_envio = models.DateField(blank=False,null=False)
    estado_envio = models.ForeignKey('EstadoEnvios',on_delete=models.CASCADE, db_column='id_estado_envio')
    
class InformesGestion(models.Model):
    id_informe = models.IntegerField(primary_key=True)
    id_empleado = models.ForeignKey('Empleados',on_delete=models.CASCADE, db_column='id_empleado')
    fecha_informe = models.DateField(blank=False,null=False)
    ventas_totales = models.IntegerField(9)
    stock_total = models.IntegerField(9)
    
class EstadosArriendo(models.Model):
    id_estado_arriendo = models.IntegerField(primary_key=True)
    estado_arriendo = models.CharField(max_length=20)
    
class Arriendos(models.Model):
    id_arriendo = models.IntegerField(primary_key=True)
    id_cliente = models.ForeignKey('Clientes',on_delete=models.CASCADE, db_column='id_cliente')
    id_producto = models.ForeignKey('Productos',on_delete=models.CASCADE, db_column='id_producto')
    fecha_inicio = models.DateField(blank=False,null=False)
    fecha_fin = models.DateField(blank=False,null=False)
    forma_pago = models.CharField(max_length=20)
    deposito_garantia = models.IntegerField(9)
    estado_arriendo = models.ForeignKey('EstadosArriendo',on_delete=models.CASCADE, db_column='id_estado_arriendo')
    
class EstadosReparacion(models.Model):
    id_estado_reparacion = models.IntegerField(primary_key=True)
    estado_reparacion = models.CharField(max_length=20)
    
class Reparaciones(models.Model):
    id_reparacion = models.IntegerField(primary_key=True),
    id_cliente = models.ForeignKey('Clientes',on_delete=models.CASCADE, db_column='id_cliente')
    id_empleado = models.ForeignKey('Empleados',on_delete=models.CASCADE, db_column='id_empleado')
    fecha_solicitud = models.DateField(blank=False,null=False),
    fecha_reparacion = models.DateField(blank=False,null=False),
    descripcion_problema = models.CharField(max_length=200),
    estado_reparacion = models.ForeignKey('EstadosReparacion',on_delete=models.CASCADE, db_column='id_estado_reparacion')
    costo_reparacion = models.IntegerField(9),
    
class HistorialMantenciones(models.Model):
    id_historial = models.IntegerField(primary_key=True),
    id_cliente = models.ForeignKey('Clientes',on_delete=models.CASCADE, db_column='id_cliente')
    id_producto = models.ForeignKey('Productos',on_delete=models.CASCADE, db_column='id_producto')
    fecha_mantencion = models.DateField(blank=False,null=False),
    descripcion_mantencion = models.CharField(max_length=200)
    
class Eventos(models.Model):
    id_evento = models.IntegerField(primary_key=True)
    nombre_evento = models.CharField(max_length=20)
    
class TrazabilidadEnvios(models.Model):
    id_trazabilidad = models.IntegerField(primary_key=True)
    id_envio = models.ForeignKey('Envios',on_delete=models.CASCADE, db_column='id_envio')
    fecha = models.DateField(blank=False,null=False)
    evento = models.ForeignKey('Eventos',on_delete=models.CASCADE, db_column='id_evento')
    
class TipoPromocion(models.Model):
    id_tipo_promo = models.IntegerField(primary_key=True)
    tipo_promo = models.CharField(max_length=20)
    
class Promociones(models.Model):
    id_promocion = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    fecha_inicio = models.DateField(blank=False,null=False)
    fecha_fin = models.DateField(blank=False,null=False)
    descuento = models.IntegerField(9)
    tipo_promocion = models.ForeignKey('TipoPromocion',on_delete=models.CASCADE, db_column='id_tipo_promo')