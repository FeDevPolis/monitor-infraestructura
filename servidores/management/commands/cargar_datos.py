from django.core.management.base import BaseCommand
from servidores.models import Servidor

class Command(BaseCommand):
    help = 'Carga datos iniciales de servidores'

    def handle(self, *args, **kwargs):
        if Servidor.objects.count() == 0:
            Servidor.objects.create(
                nombre='Web-Server-01',
                ip='192.168.1.10',
                estado='activo',
                descripcion='Servidor web principal'
            )
            Servidor.objects.create(
                nombre='DB-Server-01',
                ip='192.168.1.20',
                estado='activo',
                descripcion='Base de datos principal'
            )
            Servidor.objects.create(
                nombre='Backup-Server-01',
                ip='192.168.1.30',
                estado='mantenimiento',
                descripcion='Servidor de respaldo'
            )
            self.stdout.write(self.style.SUCCESS('Datos cargados correctamente'))
        else:
            self.stdout.write('Ya existen datos, no se cargaron nuevos registros')