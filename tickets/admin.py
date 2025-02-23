from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Ticket
from trabajadores.models import Trabajador
from empresas.models import Empresa

admin.site.register(Ticket)
admin.site.register(Trabajador)
admin.site.register(Empresa)