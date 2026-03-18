# Imagen base: Python 3.12 sobre Linux
FROM python:3.12-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar e instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del proyecto
COPY . .

# Recopilar archivos estáticos para producción
RUN python manage.py collectstatic --noinput

# Exponer el puerto
EXPOSE 8000

# Comando para arrancar el servidor
CMD ["gunicorn", "monitor.wsgi:application", "--bind", "0.0.0.0:8000"]