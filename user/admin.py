from django.contrib import admin
from django.contrib.auth.models import Permission
from .models import *

admin.site.register(Permission)
admin.site.register(User)
admin.site.register(TipoUser)