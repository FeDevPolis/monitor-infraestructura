from rest_framework import viewsets
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Servidor
from .serializers import ServidorSerializer
import google.generativeai as genai
import json
import os

class ServidorViewSet(viewsets.ModelViewSet):
    queryset = Servidor.objects.all()
    serializer_class = ServidorSerializer

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def analizar_infraestructura(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            servidores = data.get('servidores', [])
            
            resumen = "\n".join([
                f"- {s['nombre']} (IP: {s['ip']}): estado={s['estado']} - {s['descripcion']}"
                for s in servidores
            ])

            prompt = f"""Analizá este estado actual de servidores de infraestructura y dá recomendaciones específicas:

{resumen}

IMPORTANTE:
- Mencioná cada servidor por nombre y su estado actual
- NO incluyas frases introductorias como "Como experto..."
- Respondé directamente con el análisis
- Usá español técnico y conciso"""

            genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))
            model = genai.GenerativeModel('gemini-2.5-flash')
            response = model.generate_content(prompt)
            
            return JsonResponse({'respuesta': response.text})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Método no permitido'}, status=405)