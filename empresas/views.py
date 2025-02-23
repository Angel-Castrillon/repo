from django.shortcuts import render
from rest_framework import serializers, viewsets, permissions
from .models import Empresa
from .serializers import Empresas_serializer

# Create your views here.
class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'

# Vista para crear tickets desde Trabajador
class CrearEmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.filter(codEmpresa__isnull=False)
    serializer_class = EmpresaSerializer
    permission_classes = [permissions.IsAuthenticated]
