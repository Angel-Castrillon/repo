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
        cod_trabajador = self.request.data.get('codTrabajador')
        if not cod_trabajador:
            raise serializers.ValidationError({'error': 'El campo codTrabajador es requerido.'})
       
        try:
            trabajador = Trabajador.objects.get(pk=cod_trabajador)
            serializer.save(codTrabajador=trabajador)
        except Trabajador.DoesNotExist:
            raise serializers.ValidationError({'error': 'No existe un trabajador con ese código.'})

# Vista para crear tickets desde Empresa
class TicketEmpresaViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.filter(codEmpresa__isnull=False)
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        cod_empresa = self.request.data.get('codEmpresa')
        if not cod_empresa:
            raise serializers.ValidationError({'error': 'El campo codEmpresa es requerido.'})
        
        try:
            empresa = Empresa.objects.get(pk=cod_empresa)
            serializer.save(codEmpresa=empresa)
        except Empresa.DoesNotExist:
            raise serializers.ValidationError({'error': 'No existe una empresa con ese código.'})