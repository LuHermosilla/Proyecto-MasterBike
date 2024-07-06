from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import UserRegisterForm
from .models import *
from .Carrito import Carrito

# Create your views here.

def index(request):
    user = request.user
    print(user)
    context = {'user':user}                                                           
    return render(request,'gestion/index.html',context)

def error_404(request, exception):
    return render(request, 'gestion/error404.html', status=404)

def login_sesion(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["contrasena"]
        user = authenticate(username=username,password=password)
        if user is not None:
            print("Usuario autenticado...")
            login(request, user)
            return redirect('index')
        else:
            return render(request,'gestion/Login.html')
    else:
        return render(request,'gestion/Login.html')

def logout_sesion(request):
    try:
        logout(request)
        return redirect('index')
    except:
        print("Error, no se pudo cerrar sesion...")
        return redirect('index')

def Agendar(request):
    context={}
    return render(request,'gestion/Agendar.html',context)

def ConsultaStock(request):
    context={}
    return render(request,'gestion/ConsultaStock.html',context)

#Bloque de vistas crud empleados
def empleados_add(request):
    if request.method != "POST":
        sucursales = Sucursales.objects.all()
        cargos = Cargos.objects.all()
        empleados = Empleado.objects.all()
        context={"sucursales":sucursales,"cargos":cargos,"empleados":empleados}
        return render(request,'gestion/AgregarEmpleados.html',context)
    else:
        nombre=request.POST["nombre"]
        aPaterno=request.POST["apellidoPat"]
        aMaterno=request.POST["apellidoMat"]
        rut=int(request.POST["rut"])
        dv=request.POST["dv"]
        cargo=request.POST["cargo"]
        sucursal=request.POST["sucursal"]
        
        objCargo=Cargos.objects.get(id_cargo=cargo)
        objSucursal=Sucursales.objects.get(id_sucursal=sucursal)
        
        empleado = Empleado.objects.create(nombre_emp=nombre,
                                            aPaterno_emp=aPaterno,
                                            aMaterno_emp=aMaterno,
                                            rut_emp=rut,
                                            dv=dv,
                                            id_cargo=objCargo,
                                            id_sucursal=objSucursal)
        empleado.save()
    
        context={'mensaje':"Ok, datos grabados..."}
        return render(request,'gestion/AgregarEmpleados.html',context)

def empleados_list(request):
    sucursales = Sucursales.objects.all()
    cargos = Cargos.objects.all()
    empleados = Empleado.objects.all()
    
    context={"sucursales":sucursales,"cargos":cargos,"empleados":empleados}
    return render(request,'gestion/ListaEmpleados.html',context)
    
def empleados_del(request,pk):
    sucursales = Sucursales.objects.all()
    cargos = Cargos.objects.all()
    
    context={}
    
    try:
        empleado=Empleado.objects.get(id_empleado=pk)
        
        empleado.delete() 
        empleados = Empleado.objects.all()
        context={"sucursales":sucursales,"cargos":cargos,"empleados":empleados}
        return render(request,'gestion/ListaEmpleados.html',context)
    except:
        empleados = Empleado.objects.all()
        context={"sucursales":sucursales,"cargos":cargos,"empleados":empleados}
        return render(request,'gestion/ListaEmpleados.html',context)
    
def empleados_edit(request,pk):
    sucursales = Sucursales.objects.all()
    cargos = Cargos.objects.all()
    
    if pk != "":
        empleado=Empleado.objects.get(id_empleado=pk)
        context={"sucursales":sucursales,"cargos":cargos,"empleado":empleado}
        if empleado:
            return render(request,'gestion/EditarEmpleados.html',context)
        else:
            context={'mensaje':"Error, id no existe..."}
            return render(request,'gestion/ListaEmpleados.html',context)
    
def empleados_update(request):
    sucursales = Sucursales.objects.all()
    cargos = Cargos.objects.all()
    
    if request.method == "POST":
        nombre=request.POST["nombre"]
        aPaterno=request.POST["apellidoPat"]
        aMaterno=request.POST["apellidoMat"]
        rut=int(request.POST["rut"])
        dv=request.POST["dv"]
        cargo=request.POST["cargo"]
        sucursal=request.POST["sucursal"]
        
        objCargo=Cargos.objects.get(id_cargo=cargo)
        objSucursal=Sucursales.objects.get(id_sucursal=sucursal)
        
        empleado = Empleado()
        empleado.nombre_emp=nombre
        empleado.aPaterno_emp=aPaterno
        empleado.aMaterno_emp=aMaterno
        empleado.rut_emp=rut
        empleado.dv=dv
        empleado.id_cargo=objCargo
        empleado.id_sucursal=objSucursal
        
        empleado.save()
        context={'mensaje':"Ok, datos actualizados...","sucursales":sucursales,"cargos":cargos,"empleado":empleado}
        return render(request,'gestion/EditarEmpleados.html',context)
    else:
        empleados =Empleado.objects.all()
        context={"empleados":empleados}
        return render(request,"gestion/ListaEmpleados.html",context)
        
#Bloque de vistas crud productos
def productos_add(request):
    if request.method != "POST":
        categorias = CategoriaProducto.objects.all()
        proveedores = Proveedores.objects.all()
        context={"categorias":categorias, "proveedores":proveedores}
        return render(request,'gestion/AgregarProductos.html',context)
    else:
        nombre=request.POST["nombre"]
        categoria=request.POST["categoria"]
        precio_unit=request.POST["precio_unitario"]
        impuesto=request.POST["impuesto"]
        stock_actual=request.POST["stock_actual"]
        proveedor=request.POST["id_proveedor"]
        
        objCategoria = CategoriaProducto.objects.get(id_categoria = categoria)
        objProveedor = Proveedores.objects.get(id_proveedor = proveedor)
        
        prod = Producto.objects.create(nombre_prod=nombre,
                                            id_categoria=objCategoria,
                                            precio_unit=precio_unit,
                                            impuesto=impuesto,
                                            stock_actual=stock_actual,
                                            id_proveedor=objProveedor)
        prod.save()

        categorias = CategoriaProducto.objects.all()
        proveedores = Proveedores.objects.all()
        context={'mensaje':"Ok, datos grabados...","categorias":categorias, "proveedores":proveedores}
        return render(request,'gestion/AgregarProductos.html',context)
    
def productos_list(request):
    productos = Producto.objects.all()
    context={"productos":productos}
    return render(request,'gestion/ListaProductos.html',context)

def productos_del(request,pk):
    categorias = CategoriaProducto.objects.all()
    proveedores = Proveedores.objects.all()
    
    context={}
    
    try:
        producto=Producto.objects.get(id_producto=pk)
        
        producto.delete()
        productos = Producto.objects.all()
        context={"categorias":categorias,"proveedores":proveedores,"productos":productos}
        return render(request,'gestion/ListaProductos.html',context)
    except:
        productos = Producto.objects.all()
        context={"categorias":categorias,"proveedores":proveedores,"productos":productos}
        return render(request,'gestion/ListaProductos.html',context)

def productos_edit(request,pk):
    if pk != "":
        categorias = CategoriaProducto.objects.all()
        proveedores = Proveedores.objects.all()
        producto=Producto.objects.get(id_producto=pk)
        
        context={"categorias":categorias,"proveedores":proveedores,"producto":producto}
        if producto:
            return render(request,'gestion/EditarProductos.html',context)
        else:
            context={'mensaje':"Error, id no existe"}
            return render(request,'gestion/ListaProductos.html',context)

def productos_update(request):
    
    if request.method == "POST":
        id_prod=request.POST["id_producto"]
        nombre=request.POST["nombre"]
        categoria=request.POST["categoria"]
        precio_unit=request.POST["precio_unitario"]
        impuesto=request.POST["impuesto"]
        stock_actual=request.POST["stock_actual"]
        proveedor=request.POST["id_proveedor"]
        
        objCategoria = CategoriaProducto.objects.get(id_categoria = categoria)
        objProveedor = Proveedores.objects.get(id_proveedor = proveedor)
        
        producto = Producto()
        producto.id_producto=id_prod
        producto.nombre_prod=nombre
        producto.precio_unit=precio_unit
        producto.impuesto=impuesto
        producto.stock_actual=stock_actual
        producto.id_proveedor=objProveedor
        producto.id_categoria=objCategoria
        producto.save()
        producto = Producto.objects.get(id_producto=id_prod)
        
        categorias = CategoriaProducto.objects.all()
        proveedores = Proveedores.objects.all()
        context={'mensaje':"Ok, datos actualizados...","categorias":categorias,"proveedores":proveedores,"producto":producto}
        return render(request,"gestion/EditarProductos.html",context)
    else:
        productos=Producto.objects.all()
        context={"productos":productos}
        return render(request,"gestion/ListaProductos.html",context)

    
def Productos(request):
    context={}
    return render(request,'gestion/Productos.html',context)

def Perfiles(request):
    context={}
    return render(request,'gestion/Perfiles.html',context)

def RegistroClientes(request):
    context={}
    return render(request,'gestion/RegistroClientes.html',context)

def SolicitudArriendo(request):
    context={}
    return render(request,'gestion/SolicitudArriendo.html',context)

def SolicitudReparacion(request):
    context={}
    return render(request,'gestion/SolicitudReparacion.html',context)


#bloque funciones carrito de compra
def tienda(request):
    productos = Producto.objects.all()
    return render(request, "gestion/CarroDeCompras.html", {"productos": productos})

def agregar_producto(request,producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id_producto=producto_id)
    carrito.agregar(producto)
    return redirect("tienda")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id_producto=producto_id)
    carrito.eliminar(producto)
    return redirect("tienda")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id_producto=producto_id)
    carrito.restar(producto)
    return redirect("tienda")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("tienda")