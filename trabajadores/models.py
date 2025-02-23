from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Trabajador(models.Model):
    cargoTrabajador = models.CharField(max_length=255, blank=False, null=False)
    nombreTrabajador = models.CharField(max_length=255, blank=False, null=False)
    telTrabajador = models.CharField(max_length=255, blank=False, null=False)
    emailTrabajador = models.CharField(max_length=255, blank=False, null=False)
    perfilLaboral = models.CharField(max_length=450, blank=False, null=False)
    infoTrabajador = models.CharField(max_length=800, blank=False, null=False)
    codTrabajador = models.CharField(max_length=255, blank=False, null=False)
    imgTrabajador = models.BinaryField(null=True, blank=True) 

    def __str__(self):
        return self.codTrabajador