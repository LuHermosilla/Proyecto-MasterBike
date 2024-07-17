from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    numRut = models.IntegerField(null=True)
    dvRut = models.CharField(max_length=1, null=True)
    direccion = models.CharField(max_length=300, null=True)
    telefono = models.IntegerField(null=True)
    id_tipo = models.IntegerField(default=1)
    
class TipoUser(models.Model):
    id_tipo = models.IntegerField()
    nombre_tipo = models.CharField(max_length=20)
    
    def __str__(self):
        return str(self.nombre_tipo)
    