from django.shortcuts import render
from rest_framework import serializers, viewsets, permissions
from .models import Trabajador
from .serializers import Trabajadores_serializer

# Create your views here.
class TrabajadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trabajador
        fields = '__all__'

# Vista para crear tickets desde Trabajador
class CrearTrabajadorViewSet(viewsets.ModelViewSet):
    queryset = Trabajador.objects.filter(codTrabajador__isnull=False)
    serializer_class = TrabajadorSerializer
    permission_classes = [permissions.IsAuthenticated]