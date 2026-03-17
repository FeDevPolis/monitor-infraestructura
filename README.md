# 🖥️ Monitor de Infraestructura

Panel web para monitorear el estado de servidores en tiempo real, desarrollado como proyecto de práctica con un stack moderno de tecnologías open source.

## 🚀 Tecnologías utilizadas

| Tecnología | Rol |
|---|---|
| Python 3.12 | Lenguaje principal |
| Django 6 | Framework backend |
| Django REST Framework | API REST |
| MongoDB | Base de datos NoSQL |
| JavaScript (Vanilla) | Frontend dinámico |
| HTML5 + CSS3 | Interfaz de usuario |
| Docker + docker-compose | Containerización |
| Linux | Sistema operativo de los contenedores |

## ✨ Funcionalidades

- Visualización en tiempo real del estado de servidores
- Contadores de servidores activos, inactivos y en mantenimiento
- Cambio de estado de servidores desde el panel (sin recargar la página)
- API REST completa con endpoints GET, POST, PUT, PATCH y DELETE
- Panel de administración integrado (Django Admin)

## 📁 Estructura del proyecto
```
monitor-infraestructura/
├── monitor/          # Configuración del proyecto Django
├── servidores/       # App principal (modelos, vistas, API)
├── templates/        # HTML
├── static/
│   ├── css/          # Estilos
│   └── js/           # Lógica del frontend
├── Dockerfile        # Imagen Docker de la app
├── docker-compose.yml # Orquestación de contenedores
└── requirements.txt  # Dependencias Python
```

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

## 📡 Endpoints de la API

| Método | Endpoint | Descripción |
|---|---|---|
| GET | /api/servidores/ | Lista todos los servidores |
| POST | /api/servidores/ | Crea un nuevo servidor |
| GET | /api/servidores/{id}/ | Obtiene un servidor |
| PUT | /api/servidores/{id}/ | Actualiza un servidor |
| PATCH | /api/servidores/{id}/ | Actualiza el estado |
| DELETE | /api/servidores/{id}/ | Elimina un servidor |

## 👤 Autor

**Federico Poliseno**  
[GitHub](https://github.com/FeDevPolis)

## 📄 Licencia

Este proyecto está bajo la licencia MIT.