from django.db import models
from trabajadores.models import Trabajador  # Importar desde la app trabajadores
from empresas.models import Empresa  # Importar desde la app empresas

# Create your models here.
class Ticket(models.Model):
    idTickets = models.AutoField(primary_key=True)
    descripcion = models.TextField()
    fechaIncial = models.DateTimeField(auto_now_add=True)
    fechaRespuesta = models.DateTimeField(null=True, blank=True)
    codTrabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE, related_name='tickets', null=True, blank=True)
    codEmpresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='tickets', null=True, blank=True)

    def __str__(self):
        if self.codTrabajador:
            return f"Ticket {self.idTickets} - {self.codTrabajador.nombreTrabajador}"
        elif self.codEmpresa:
            return f"Ticket {self.idTickets} - {self.codEmpresa.nombreEmpresa}"
        return f"Ticket {self.idTickets}"
