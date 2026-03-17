from django.contrib import admin
from .models import Servidor

@admin.register(Servidor)
class ServidorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ip', 'estado', 'fecha_ultimo_chequeo')
    search_fields = ('nombre', 'ip')
    list_filter = ('estado',)