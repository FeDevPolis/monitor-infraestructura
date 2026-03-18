from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from servidores.views import ServidorViewSet, index, analizar_infraestructura

router = DefaultRouter()
router.register(r'servidores', ServidorViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/analizar/', analizar_infraestructura, name='analizar'),
]