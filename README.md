# Provilist Backend API

Este proyecto es una API REST backend construida con **Flask** (Python) que se encarga de gestionar la información geográfica de las **provincias**, **capitales** y **municipios** de Euskal Herria.

*Nota: Este repositorio o carpeta se centra exclusivamente en el Backend (API y base de datos).*

---

## 🚀 Tecnologías Principales

### Backend
- **Python 3.12**
- **Flask 3.1.3** (Framework web)
- **Flask-SQLAlchemy** (ORM para gestión de base de datos)
- **Flask-Migrate** y **Alembic** (Control de versiones de BD)
- **Flask-CORS** (Para habilitar peticiones desde el frontend)
- **SQLite** (Base de datos local)

### Frontend
- **Vue 3 (Vapor/Beta)** con **TypeScript**
- **Vite** (Herramienta de construcción y servidor de desarrollo)
- **Axios** (Cliente HTTP para consumir la API)
- **CSS Vanilla** (Diseño personalizado y moderno)

---

## 📋 Arquitectura del Proyecto

El proyecto sigue una arquitectura desacoplada y modular:

### Backend (Carpeta `app/`)
Sigue un patrón de **tres capas** para asegurar la escalabilidad:
1. **Models (`app/models/`):** Definición de la estructura de datos mediante clases de SQLAlchemy, utilizando Mixins para funcionalidades comunes (como `to_dict` y auditoría de tiempos).
2. **Services (`app/services/`):** Capa de lógica de negocio pura. Los servicios interactúan con los modelos y son llamados por las rutas.
3. **Routes (`app/routes/`):** Blueprints de Flask que manejan las peticiones HTTP y registran los endpoints de la API.

### Frontend (Carpeta `Frontend/`)
Basado en una arquitectura de componentes:
- **API Layer:** Servicios de Axios tipados con interfaces de TypeScript.
- **Components:** Tablas y formularios modulares para cada entidad geográfica.
- **Views:** Vistas principales de navegación (Provincias, Capitales, Municipios).

### Estructura de Archivos
```text
Provilist/
├── run.py                    # 🚀 Punto de entrada del Backend
├── app/                      # 🐍 Lógica del Servidor Flask
│   ├── models/               # 📊 Modelos de Datos (Provincia, Capital, Municipio)
│   ├── routes/               # 📡 Blueprints y Controladores API
│   ├── services/             # 🛠️ Lógica de Negocio
│   └── seeds/                # 🌱 Generación de datos iniciales
├── Frontend/                 # ⚡ Aplicación Vue 3 + Vite
│   ├── src/
│   │   ├── api/              # 📞 Cliente API y Servicios
│   │   ├── components/       # 🧱 Componentes UI reutilizables
│   │   └── views/            # 🖼️ Vistas de la aplicación
├── migrations/               # 🔄 Historial de migraciones de la BD
└── provilist.db              # 🗄️ Base de datos SQLite
```

---

## ⚙️ Requisitos Previos

- **Python 3.12** o superior.
- **Node.js** (v20 o superior) y **npm**.
- Controlador de paquetes `pip`.

---

## 🛠️ Instalación y Configuración

### 1. Configuración del Backend
```bash
# Acceder a la raíz del proyecto
cd Provilist

# Crear y activar entorno virtual
python3 -m venv provilistEnv
source provilistEnv/bin/activate  # Linux/macOS
# provilistEnv\Scripts\activate   # Windows

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar migraciones para crear la base de datos
flask db upgrade

# Cargar datos iniciales (opcional)
flask seed
```

### 2. Configuración del Frontend
```bash
# Acceder a la carpeta del frontend
cd Frontend

# Instalar dependencias de Node
npm install
```

---

## 🏃 Ejecución del Proyecto

Para que la aplicación funcione correctamente, deben estar corriendo tanto el servidor backend como el frontend:

### Backend (Terminal 1)
```bash
python run.py
```
La API estará disponible en `http://127.0.0.1:5000`.

### Frontend (Terminal 2)
```bash
cd Frontend
npm run dev
```
La aplicación web será accesible en `http://localhost:5173`. *Vite está configurado con un proxy para redirigir las llamadas a `/api` directamente al backend de Flask.*

---

## 🌐 Endpoints de la API

### Provincias (`/provincias`)
- `GET /provincias` - Listar todas las provincias.
- `GET /provincias/<id>` - Obtener detalles de una provincia.
- `POST /provincias` - Crear una provincia.
- `PUT /provincias/<id>` - Actualizar una provincia.
- `DELETE /provincias/<id>` - Eliminar una provincia.

### Capitales (`/capitales`)
- `GET /capitales` - Listar todas las capitales.
- `GET /capitales/<id>` - Detalles de una capital.
- `POST /capitales` - Crear nueva capital.
- `PUT /capitales/<id>` - Actualizar capital.
- `DELETE /capitales/<id>` - Eliminar capital.

### Municipios (`/municipios`)
- `GET /municipios` - Listar municipios (Soporta paginación: `?page=1&per_page=10`).
- `GET /municipios/<id>` - Detalles de un municipio.
- `POST /municipios` - Crear un nuevo municipio.
- `PUT /municipios/<id>` - Actualizar un municipio.
- `DELETE /municipios/<id>` - Eliminar municipio.

---

## 📚 Documentación Adicional

Para más detalles sobre la construcción y flujo del proyecto, consulta los siguientes archivos:
- `documentacion_tecnica_provilist.md`: Arquitectura técnica detallada y modelos.
- `manual_creacion_provilist.md`: Paso a paso del desarrollo del proyecto.

## Colaboradores

- [Stiwar](https://github.com/troyanojoi-sour)
- [Kevin](https://github.com/Kevingedev)
- [Naia](https://github.com/Naiare7)
