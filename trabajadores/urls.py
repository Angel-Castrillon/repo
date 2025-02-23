from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CrearTrabajadorViewSet

router = DefaultRouter()
router.register(r'create', CrearTrabajadorViewSet, basename='crear')

urlpatterns = [
    path('', include(router.urls)),
]