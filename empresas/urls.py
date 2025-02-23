from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CrearEmpresaViewSet

router = DefaultRouter()
router.register(r'create', CrearEmpresaViewSet, basename='crear')

urlpatterns = [
    path('', include(router.urls)),
]