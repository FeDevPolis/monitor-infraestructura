from django.db import models

class Servidor(models.Model):
    nombre = models.CharField(max_length=100)
    ip = models.CharField(max_length=15)
    estado = models.CharField(max_length=20, choices=[
        ('activo', 'Activo'), 
        ('inactivo', 'Inactivo'), 
        ('mantenimiento', 'Mantenimiento  ')
    ], default='activo')
    descripcion = models.TextField(blank=True)
    fecha_ultimo_chequeo = models.DateTimeField(auto_now=True)      
    fecha_creacion = models.DateTimeField(auto_now_add=True)    

    def __str__(self):
        return f"{self.nombre} ({self.ip})"