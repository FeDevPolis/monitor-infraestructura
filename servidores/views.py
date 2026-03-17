from rest_framework import viewsets
from django.shortcuts import render
from .models import Servidor
from .serializers import ServidorSerializer

class ServidorViewSet(viewsets.ModelViewSet):
    queryset = Servidor.objects.all()
    serializer_class = ServidorSerializer

def index(request):
    return render(request, 'index.html')