# Laboratorio 1: Arquitectura Monolítica por Capas

Este proyecto implementa un sistema de gestión de calificaciones utilizando una arquitectura monolítica organizada en capas, desplegada mediante contenedores Docker.

## Arquitectura del Sistema
El sistema sigue un patrón de diseño por capas para asegurar la separación de responsabilidades:
- **Templates**: Interfaz de usuario (Flask/Jinja2).
- **Controllers**: Gestión de rutas y peticiones.
- **Services**: Lógica de negocio intermediaria.
- **Repositories**: Abstracción del acceso a datos.
- **Models**: Definición de entidades con SQLAlchemy.

## Tecnologías Utilizadas
- **Python 3.11** (Flask & SQLAlchemy)
- **MySQL 8.0**
- **Docker & Docker Compose**
- **CachyOS (Linux)** como entorno de desarrollo.

---

## Guía de Comandos

### 1. Despliegue de la Aplicación
Para levantar el entorno completo (Contenedor de Python + Contenedor de MySQL):
```bash
# Construir imágenes y levantar servicios
docker-compose up --build

# Levantar servicios en segundo plano (Detached mode)
docker-compose up -d

# Detener y eliminar contenedores
docker-compose down