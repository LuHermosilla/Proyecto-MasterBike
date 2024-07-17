from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout,get_user_model
from .forms import *
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

@login_required
def perfil(request):
    try:
        User = get_user_model()
        print(User)
        user = User.objects.get(username=request.user)
        print(user)
        context = {}
        if user:
            print("Perfil...")
            if request.method == "POST":
                print("Edit, es un post...")
                form = UsuarioForm(request.POST,instance=request.user)
                form.save()
                return redirect('index')
            else:
                print("Edit, no es un post...")
                form = UsuarioForm(instance=request.user)
                print("Edit, no es un post...")
                mensaje = ""
                context = {"user":user,"form":form,"mensaje":mensaje}
                print("Edit, no es un post...")
                return render(request,'gestion/Perfil.html',context)
    except:
        print("Error, perfil no existe...")
        return redirect('index')

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('index')

    return render(request, 'gestion/Registro_usuario.html', data)

#Bloque de vistas crud empleados
@login_required
def empleados_add(request):
    context = {'form':EmpleadosForm}
    if request.method == 'POST':
        prov_creation_form = EmpleadosForm(data=request.POST)

        if prov_creation_form.is_valid():
            prov_creation_form.save()

            return redirect('empleados_list')
        else:
            context['form'] = prov_creation_form

    return render(request,'gestion/AgregarEmpleados.html',context)

@login_required
def empleados_list(request):
    sucursales = Sucursales.objects.all()
    cargos = Cargos.objects.all()
    empleados = Empleado.objects.all()
    
    context={"sucursales":sucursales,"cargos":cargos,"empleados":empleados}
    return render(request,'gestion/ListaEmpleados.html',context)

@login_required
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

@login_required
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

@login_required  
def empleados_update(request):

    
    if request.method == "POST":
        id_emp=request.POST["id_empleado"]
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
        empleado = Empleado.objects.get(id_empleado=id_emp)
        
        empleados = Empleado.objects.all()
        sucursales = Sucursales.objects.all()
        cargos = Cargos.objects.all()
        
        context={'mensaje':"Ok, datos actualizados...","sucursales":sucursales,"cargos":cargos,"empleado":empleado,"empleados":empleados}
        return render(request,'gestion/EditarEmpleados.html',context)
    else:
        empleados =Empleado.objects.all()
        context={"empleados":empleados}
        return render(request,"gestion/ListaEmpleados.html",context)
        
#Bloque de vistas crud productos
@login_required
def productos_add(request):
    context = {'form':ProductoForm}
    if request.method == 'POST':
        prov_creation_form = ProductoForm(data=request.POST)

        if prov_creation_form.is_valid():
            prov_creation_form.save()

            return redirect('productos_list')
        else:
            context['form'] = prov_creation_form

    return render(request, 'gestion/AgregarProductos.html', context)
 
@login_required   
def productos_list(request):
    productos = Producto.objects.all()
    context={"productos":productos}
    return render(request,'gestion/ListaProductos.html',context)

@login_required
def productos_del(request,pk):
    categorias = CategoriaProducto.objects.all()
    proveedores = Proveedor.objects.all()
    
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

@login_required
def productos_edit(request,pk):
    if pk != "":
        categorias = CategoriaProducto.objects.all()
        proveedores = Proveedor.objects.all()
        producto=Producto.objects.get(id_producto=pk)
        
        context={"categorias":categorias,"proveedores":proveedores,"producto":producto}
        if producto:
            return render(request,'gestion/EditarProductos.html',context)
        else:
            context={'mensaje':"Error, id no existe"}
            return render(request,'gestion/ListaProductos.html',context)

@login_required
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
        objProveedor = Proveedor.objects.get(id_proveedor = proveedor)
        
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
        proveedores = Proveedor.objects.all()
        context={'mensaje':"Ok, datos actualizados...","categorias":categorias,"proveedores":proveedores,"producto":producto}
        return render(request,"gestion/EditarProductos.html",context)
    else:
        productos=Producto.objects.all()
        context={"productos":productos}
        return render(request,"gestion/ListaProductos.html",context)

#Bloque de vistas crud proveedores
@login_required 
def proveedores_add(request):
    context = {'form':ProveedorForm}
    if request.method == 'POST':
        prov_creation_form = ProveedorForm(data=request.POST)

        if prov_creation_form.is_valid():
            prov_creation_form.save()

            return redirect('proveedores_list')
        else:
            context['form'] = prov_creation_form

    return render(request, 'gestion/AgregarProveedores.html', context)

@login_required    
def proveedores_list(request):
    proveedores = Proveedor.objects.all()
    context={"proveedores":proveedores}
    return render(request,'gestion/ListaProveedores.html',context)

@login_required
def proveedores_del(request,pk):
    
    context={}
    
    try:
        proveedor=Proveedor.objects.get(id_proveedor=pk)
        
        proveedor.delete()
        proveedores = Proveedor.objects.all()
        context={"proveedores":proveedores}
        return render(request,'gestion/ListaProveedores.html',context)
    except:
        proveedores = Proveedor.objects.all()
        context={"proveedores":proveedores}
        return render(request,'gestion/ListaProveedores.html',context)

@login_required
def proveedores_edit(request,pk):
    if pk != "":
        proveedor=Proveedor.objects.get(id_proveedor=pk)
        
        context={"proveedor":proveedor}
        if proveedor:
            return render(request,'gestion/EditarProveedores.html',context)
        else:
            context={'mensaje':"Error, id no existe"}
            return render(request,'gestion/ListaProveedores.html',context)

@login_required
def proveedores_update(request):
    
    if request.method == "POST":
        id_prov=request.POST["id_proveedor"]
        nombre=request.POST["nombre"]
        rut=request.POST["rut"]
        direccion=request.POST["direccion"]
        telefono=request.POST["telefono"]
        web=request.POST["PaginaWeb"]
        email=request.POST["email"]
        
        
        proveedor = Proveedor()
        proveedor.id_proveedor=id_prov
        proveedor.nombre_prov=nombre
        proveedor.rut_prov=rut
        proveedor.direccion=direccion
        proveedor.telefono=telefono
        proveedor.pagina_web=web
        proveedor.email=email
        proveedor.save()
        
        proveedor = Proveedor.objects.get(id_proveedor=id_prov)
        
        context={'mensaje':"Ok, datos actualizados...","proveedor":proveedor}
        return render(request,"gestion/EditarProveedores.html",context)
    else:
        proveedores=Proveedor.objects.all()
        context={"proveedores":proveedores}
        return render(request,"gestion/ListaProveedores.html",context)

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

#despacho
def mostrar_despachos(request):
    context={}
    return render(request,'gestion/Despacho.html',context)

def Inventario(request):
    productos = Producto.objects.all()
    context={"productos":productos}
    return render(request,'gestion/Inventario.html',context)

#ventas
def procesar_carrito(request):
    carrito = Carrito(request)
    User = get_user_model()
    usuario = User.objects.get(username=request.user)
    
    context = {"usuario":usuario}
    return render(request,"gestion/ConfirmacionPedido.html",context)

#TO DO

def SolicitudArriendo(request):
    context={}
    return render(request,'gestion/SolicitudArriendo.html',context)

def SolicitudReparacion(request):
    context={}
    return render(request,'gestion/SolicitudReparacion.html',context)

def Agendar(request):
    context={}
    return render(request,'gestion/Agendar.html',context)

def ConsultaStock(request):
    context={}
    return render(request,'gestion/ConsultaStock.html',context)