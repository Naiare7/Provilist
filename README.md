# Provilist Backend API

Este proyecto es una API REST backend construida con **Flask** (Python) que se encarga de gestionar la información geográfica de las **provincias**, **capitales** y **municipios** de Euskal Herria.

*Nota: Este repositorio o carpeta se centra exclusivamente en el Backend (API y base de datos).*

---

## 🚀 Tecnologías Principales

- **Python 3.12**
- **Flask** 3.1.3 (Framework web)
- **Flask-SQLAlchemy** (ORM)
- **Flask-Migrate** y **Alembic** (Control de versiones de la BD y Migraciones)
- **SQLite** (Base de datos)

---

## 📋 Arquitectura del Proyecto

El proyecto sigue una arquitectura sólida basada en **tres capas** para facilitar la mantenibilidad y la separación de responsabilidades:

1. **Routes (Rutas):** Define los endpoints de la API mediante Blueprints de Flask y maneja las peticiones/respuestas HTTP.
2. **Services (Servicios):** Contiene la lógica de negocio pura de la aplicación. Las rutas llaman a los servicios.
3. **Models (Modelos):** Define la estructura de los datos que se guardan en la base de datos a través de SQLAlchemy.

### Estructura de Carpetas

```text
Provilist/
├── run.py                    # 🚀 Punto de entrada de la aplicación
├── requirements.txt          # 📦 Dependencias del proyecto
├── provilist.db              # 🗄️ Base de datos SQLite local
├── app/
│   ├── __init__.py           # 🏭 Factory de la aplicación Flask
│   ├── config.py             # ⚙️ Configuración (BD, etc.)
│   ├── models.py             # 📊 Modelos (Provincia, Capital, Municipio)
│   ├── routes/               # 📡 Blueprints y Controladores
│   ├── services/             # 🛠️ Lógica de negocio
│   └── seeds/                # 🌱 Datos iniciales para la base de datos
└── migrations/               # 🔄 Archivos de migración de Alembic
```

---

## ⚙️ Requisitos Previos

- Python 3.12 o superior.
- Controlador de paquetes `pip`.

---

## 🛠️ Instalación y Configuración

Sigue estos pasos para ejecutar la API localmente en tu máquina:

### 1. Clonar el repositorio y acceder a la carpeta

```bash
cd Provilist
```

### 2. Crear y activar el entorno virtual

```bash
# Crear entorno virtual
python3 -m venv provilistEnv

# Activar en Linux / macOS:
source provilistEnv/bin/activate

# Activar en Windows:
provilistEnv\Scripts\activate
```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 4. Inicializar la Base de Datos (Migraciones)

La estructura de las tablas se maneja a través de migraciones automatizadas:

```bash
flask db upgrade
```

### 5. Cargar los Datos Iniciales (Seeds)

*Si las opciones de comandos están habilitadas en `run.py`.*
```bash
flask seed
```

---

## 🏃 Ejecución de la API

Para lanzar el servidor de desarrollo, ejecuta el siguiente comando:

```bash
python run.py
```

La API estará disponible localmente en `http://127.0.0.1:5000`.

---

## 🌐 Endpoints Principales

Aquí tienes un breve resumen de los endpoints disponibles en la API:

### Provincias (`/provincias`)
- `GET /provincias` - Listar todas las provincias.
- `POST /provincias` - Crear una nueva provincia.
- `PUT /provincias/<id>` - Actualizar datos de una provincia.
- `DELETE /provincias/<id>` - Eliminar provincia.

### Capitales (`/capitales`)
- `GET /capitales` - Listar todas las capitales.
- `POST /capitales` - Crear nueva capital.
- `PUT /capitales/<id>` - Actualizar datos de una capital.
- `DELETE /capitales/<id>` - Eliminar capital.

### Municipios (`/municipios`)
- `GET /municipios` - Listar todos los municipios.
- `POST /municipios` - Crear un nuevo municipio.
- `PUT /municipios/<id>` - Actualizar datos de un municipio.
- `DELETE /municipios/<id>` - Eliminar municipio.

---

## 📚 Documentación Adicional

Dentro del directorio existen manuales más técnicos y detallados si necesitas modificar la API o profundizar en cómo está construida:

- `documentacion_tecnica_provilist.md`: Detalles de la DB, modelos, flujos completos y comandos técnicos.
- `manual_creacion_provilist.md`: Guía de construcción desde cero y explicación paso a paso de las partes del código fuente.

## Colaboradores

- [Naia](https://github.com/Naiare7)

