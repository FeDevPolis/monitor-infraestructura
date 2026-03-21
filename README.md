# 🖥️ Monitor de Infraestructura

Panel web para monitorear el estado de servidores en tiempo real, desarrollado como proyecto de práctica con un stack moderno de tecnologías open source.

---

## 🎯 Objetivo

Este proyecto fue desarrollado como práctica para simular un sistema real de monitoreo de infraestructura, integrando backend, base de datos, frontend y despliegue en contenedores.

El objetivo principal fue entender cómo se construye una aplicación completa que permita visualizar, gestionar y analizar el estado de servicios en un entorno centralizado.

---

## 🌐 Demo en vivo

[https://monitor-infraestructura.onrender.com](https://monitor-infraestructura.onrender.com)

---

## 🚀 Tecnologías utilizadas

| Tecnología | Rol |
|---|---|
| Python 3.12 | Lenguaje principal |
| Django 6 | Framework backend |
| Django REST Framework | API REST |
| MongoDB Atlas | Base de datos NoSQL en la nube |
| JavaScript (Vanilla) | Frontend dinámico |
| HTML5 + CSS3 | Interfaz de usuario |
| Docker + docker-compose | Containerización |
| Linux | Sistema operativo de los contenedores |
| Gunicorn | Servidor WSGI de producción |
| Whitenoise | Archivos estáticos en producción |
| Gemini API (Google) | Análisis de infraestructura con IA |

---

## 🏗️ Arquitectura

- Backend: Django + Django REST Framework  
- Base de datos: MongoDB Atlas (NoSQL)  
- Frontend: HTML + CSS + JavaScript  
- Contenerización: Docker + Docker Compose  
- Servidor: Gunicorn + Whitenoise  

---

## ✨ Funcionalidades

- Visualización en tiempo real del estado de servidores
- Contadores de servidores activos, inactivos y en mantenimiento
- Cambio de estado de servidores desde el panel (sin recargar la página)
- API REST completa con endpoints GET, POST, PUT, PATCH y DELETE
- Panel de administración integrado (Django Admin)
- Asistente de IA integrado con Gemini API para análisis del estado de la infraestructura

---

## 🧠 Decisiones técnicas

- Se utilizó MongoDB por su flexibilidad para manejar estructuras de datos dinámicas.  
- Se implementó una API REST para desacoplar frontend y backend.  
- Se utilizó Docker para garantizar portabilidad y consistencia del entorno.  
- Se integró una API de IA (Gemini) para explorar análisis automatizado de datos.  

---

## 📁 Estructura del proyecto
```
monitor-infraestructura/
├── monitor/          # Configuración del proyecto Django
├── servidores/       # App principal (modelos, vistas, API)
├── templates/        # HTML
├── static/
│   ├── css/
│   │   ├── monitor.css       # Estilos principales
│   │   └── chat.css          # Estilos del asistente IA
│   └── js/
│       ├── monitor.js        # Lógica del frontend
│       └── chat.js           # Lógica del asistente IA
├── Dockerfile        # Imagen Docker de la app
├── docker-compose.yml # Orquestación de contenedores
└── requirements.txt  # Dependencias Python
```

---

## ⚙️ Instalación y uso

### Con Docker (recomendado)

1. Cloná el repositorio:
```bash
git clone https://github.com/FeDevPolis/monitor-infraestructura.git
cd monitor-infraestructura
```

2. Levantá los contenedores:
```bash
docker-compose up --build
```

3. Entrá a http://localhost:8000

### Sin Docker

1. Cloná el repositorio e instalá dependencias:
```bash
git clone https://github.com/FeDevPolis/monitor-infraestructura.git
cd monitor-infraestructura
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

2. Aplicá las migraciones:
```bash
python manage.py migrate
```

3. Creá un superusuario:
```bash
python manage.py createsuperuser
```

4. Arrancá el servidor:
```bash
python manage.py runserver
```

5. Entrá a http://localhost:8000

---

## 📡 Endpoints de la API

| Método | Endpoint | Descripción |
|---|---|---|
| GET | /api/servidores/ | Lista todos los servidores |
| POST | /api/servidores/ | Crea un nuevo servidor |
| GET | /api/servidores/{id}/ | Obtiene un servidor |
| PUT | /api/servidores/{id}/ | Actualiza un servidor |
| PATCH | /api/servidores/{id}/ | Actualiza el estado |
| DELETE | /api/servidores/{id}/ | Elimina un servidor |
| POST | /api/analizar/ | Envía datos al asistente IA con Gemini |

---

## 👤 Autor

**Federico Poliseno**  
[GitHub](https://github.com/FeDevPolis)

---

## 📄 Licencia

Este proyecto está bajo la licencia MIT.