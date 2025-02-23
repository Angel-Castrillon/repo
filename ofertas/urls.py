from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CrearOfertaViewSet

router = DefaultRouter()
router.register(r'create', CrearOfertaViewSet, basename='crear')

urlpatterns = [
    path('', include(router.urls)),
]