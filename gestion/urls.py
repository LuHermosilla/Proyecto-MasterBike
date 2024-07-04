from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    
    #carrito de compra
    path('tienda', views.tienda, name='tienda'),
    path('agregar_producto/<int:producto_id>/', views.agregar_producto, name="Add"),
    path('eliminar_producto/<int:producto_id>/', views.eliminar_producto, name="Del"),
    path('restar_producto/<int:producto_id>/', views.restar_producto, name="Sub"),
    path('limpiar_carrito/', views.limpiar_carrito, name="CLS"),
    
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
    
    #login
    path('login_sesion', views.login_sesion, name='login_sesion'),
    path('logout_sesion', views.logout_sesion, name='logout_sesion'),
    
    
    path('ConsultaStock', views.ConsultaStock, name='ConsultaStock'),
    path('Agendar', views.Agendar, name='Agendar'),
    path('Perfiles', views.Perfiles, name='Perfiles'),
    path('RegistroClientes', views.RegistroClientes, name='RegistroClientes'),
    path('SolicitudArriendo', views.SolicitudArriendo, name='SolicitudArriendo'),
    path('SolicitudReparacion', views.SolicitudReparacion, name='SolicitudReparacion'),
]
