from rest_framework import serializers, viewsets, permissions
from .models import Ticket
from trabajadores.models import Trabajador
from empresas.models import Empresa

# Serializador para Tickets
class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

# Vista para crear tickets desde Trabajador
class TicketTrabajadorViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.filter(codTrabajador__isnull=False)
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        trabajador = Trabajador.objects.get(user=self.request.user)
        serializer.save(codTrabajador=trabajador)

# Vista para crear tickets desde Empresa
class TicketEmpresaViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.filter(codEmpresa__isnull=False)
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        empresa = Empresa.objects.get(emailEmpresa=self.request.user.email)
        serializer.save(codEmpresa=empresa)