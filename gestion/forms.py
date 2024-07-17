from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import *
from user.models import User

from django.forms import ModelForm
    
#Formulario usado en vista perfil    
class UsuarioForm(ModelForm):
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email','numRut','dvRut','direccion','telefono']
        widgets = { 'first_name':forms.TextInput(attrs={'class':'form-control'}),
                    'last_name':forms.TextInput(attrs={'class':'form-control'}),
                    'email':forms.EmailInput(attrs={'class':'form-control'}),
                    'numRut':forms.NumberInput(attrs={'class':'form-control'}),
                    'dvRut':forms.NumberInput(attrs={'class':'form-control'}),
                    'direccion':forms.TextInput(attrs={'class':'form-control'}),
                    'telefono':forms.NumberInput(attrs={'class':'form-control'}),
                   }
                   
#Formulario usado en registro de usuario
class CustomUserCreationForm(UserCreationForm):
	
	class Meta:
		User = get_user_model()
		model = User
		fields = [
                    'username',
                    'first_name',
                    'last_name',
                    'email',
                    'password1',
                    'password2',
                    'numRut',
                    'dvRut',
                    'direccion',
                    'telefono'
                    ]
  
  
class ProductoForm(ModelForm):
    
    class Meta:
        model = Producto
        fields = ['nombre_prod','id_categoria','precio_unit','impuesto','stock_actual','id_proveedor']
        
class ProveedorForm(ModelForm):
    
    class Meta:
        model = Proveedor
        fields = ['nombre_prov','rut_prov','direccion','telefono','pagina_web','email']
        widgets = {'nombre_prov':forms.TextInput(attrs={'class':'form-control'}),
                   'rut_prov':forms.TextInput(attrs={'class':'form-control'}),
                   'direccion':forms.TextInput(attrs={'class':'form-control'}),
                   'telefono':forms.NumberInput(attrs={'class':'form-control'}),
                   'pagina_web':forms.TextInput(attrs={'class':'form-control'}),
                   'email':forms.EmailInput(attrs={'class':'form-control'})}
        
class EmpleadosForm(ModelForm):
    aPaterno_emp = forms.CharField(label="Apellido Paterno")
    aMaterno_emp = forms.CharField(label="Apellido Materno")
    
    class Meta:
        model = Empleado
        fields = ['nombre_emp','aPaterno_emp','aMaterno_emp','rut_emp','dv','id_cargo','id_sucursal']
        
        