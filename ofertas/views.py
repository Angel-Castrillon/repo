from django.shortcuts import render
from rest_framework import serializers, viewsets, permissions
from .models import Oferta
from .serializers import Ofertas_serializer

# Create your views here.
class OfertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oferta
        fields = '__all__'

# Vista para crear tickets desde Trabajador
class CrearOfertaViewSet(viewsets.ModelViewSet):
    queryset = Oferta.objects.filter(codOferta__isnull=False)
    serializer_class = OfertaSerializer
    permission_classes = [permissions.IsAuthenticated]
    