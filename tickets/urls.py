from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TicketTrabajadorViewSet, TicketEmpresaViewSet

router = DefaultRouter()
router.register(r'trabajador', TicketTrabajadorViewSet, basename='ticket-trabajador')
router.register(r'empresa', TicketEmpresaViewSet, basename='ticket-empresa')

urlpatterns = [
    path('', include(router.urls)),
]