from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    
    #carrito de compra
    path('tienda', views.tienda, name='tienda'),
    path('agregar_producto/<int:producto_id>/', views.agregar_producto, name="carrito_Add"),
    path('eliminar_producto/<int:producto_id>/', views.eliminar_producto, name="Del"),
    path('restar_producto/<int:producto_id>/', views.restar_producto, name="carrito_Sub"),
    path('limpiar_carrito/', views.limpiar_carrito, name="carrito_CLS"),
    
    #crud empleados
    path('empleados_add', views.empleados_add, name='empleados_add'),
    path('empleados_list', views.empleados_list, name='empleados_list'),
    path('empleados_del/<str:pk>',views.empleados_del,name='empleados_del'),
    path('empleados_edit/<str:pk>',views.empleados_edit,name='empleados_edit'),
    path('empleados_update',views.empleados_update,name='empleados_update'),
    
    #crud productos
    path('productos_add', views.productos_add, name='productos_add'),
    path('productos_list', views.productos_list, name='productos_list'),
    path('productos_del/<str:pk>',views.productos_del,name='productos_del'),
    path('productos_edit/<str:pk>',views.productos_edit,name='productos_edit'),
    path('productos_update',views.productos_update,name='productos_update'),
    
    #crud proveedores
    path('proveedores_add', views.proveedores_add, name='proveedores_add'),
    path('proveedores_list', views.proveedores_list, name='proveedores_list'),
    path('proveedores_del/<str:pk>',views.proveedores_del,name='proveedores_del'),
    path('proveedores_edit/<str:pk>',views.proveedores_edit,name='proveedores_edit'),
    path('proveedores_update',views.proveedores_update,name='proveedores_update'),
    
    #login
    path('login_sesion', views.login_sesion, name='login_sesion'),
    path('logout_sesion', views.logout_sesion, name='logout_sesion'),
    
    #registro
    path('registro', views.registro, name='registro'),
    
    #perfil
    path('perfil', views.perfil, name='perfil'),
      
    path('procesar_carrito', views.procesar_carrito, name='procesar_carrito'),
    
    
    path('mostrar_despachos', views.mostrar_despachos, name='mostrar_despachos'),
    
    path('Inventario', views.Inventario, name='Inventario'),
    path('ConsultaStock', views.ConsultaStock, name='ConsultaStock'),
    path('Agendar', views.Agendar, name='Agendar'),
    path('SolicitudArriendo', views.SolicitudArriendo, name='SolicitudArriendo'),
    path('SolicitudReparacion', views.SolicitudReparacion, name='SolicitudReparacion'),
]
