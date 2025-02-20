# API de Gestión de Programadores 👨‍💻

Una API REST moderna y eficiente para gestionar la información de programadores en una empresa, construida con Django REST Framework.

## 🚀 Características

- CRUD completo para gestión de programadores
- Documentación automática de la API
- Interfaz de administración integrada
- Endpoints RESTful
- Filtrado y búsqueda de programadores
- Soporte para formato JSON

## 🛠️ Tecnologías Utilizadas

- Python 3.x
- Django 4.2.6
- Django REST Framework 3.14.0
- SQLite (Base de datos)
- Core API (Documentación)

## 📋 Requisitos Previos

- Python 3.x instalado
- pip (gestor de paquetes de Python)
- Entorno virtual (recomendado)

## ⚙️ Instalación

1. Clona el repositorio:
```bash
git clone [URL del repositorio]
cd primera-api
```

2. Crea y activa un entorno virtual (opcional pero recomendado):
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. Instala las dependencias:
```bash
pip install -r requirements.txt
```

4. Ejecuta las migraciones:
```bash
python manage.py migrate
```

5. Crea un superusuario (opcional):
```bash
python manage.py createsuperuser
```

6. Inicia el servidor:
```bash
python manage.py runserver
```

## 🔍 Uso de la API

### Endpoints Disponibles

- `GET /api/programmers/`: Lista todos los programadores
- `POST /api/programmers/`: Crea un nuevo programador
- `GET /api/programmers/{id}/`: Obtiene detalles de un programador específico
- `PUT /api/programmers/{id}/`: Actualiza un programador existente
- `DELETE /api/programmers/{id}/`: Elimina un programador

### Estructura de Datos

```json
{
    "fullname": "Nombre Completo",
    "nickname": "Apodo",
    "age": 25,
    "is_active": true
}
```

## 📚 Documentación

La documentación completa de la API está disponible en:
- `/docs/`: Documentación interactiva de la API
- `/admin/`: Panel de administración (requiere credenciales)

## 🤝 Contribuir

Las contribuciones son bienvenidas. Por favor, siéntete libre de:

1. Fork el proyecto
2. Crear una rama para tu característica
3. Commit tus cambios
4. Push a la rama
5. Abrir un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia [Especificar licencia]

---
⌨️ con ❤️ por David Alejandro Chentes