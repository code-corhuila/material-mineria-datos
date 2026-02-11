# 🌡️ ETL Weatherstack - Tutorial Completo

## Descripción General

Este es un **tutorial completo y funcional** que te mostrará cómo crear un **pipeline ETL profesional** (Extract, Transform, Load) usando datos de clima de la API Weatherstack. 

El proyecto cubre los **4 pasos esenciales**:

1. ✅ **Alistamiento de WSL Ubuntu 24 en Windows**
2. ✅ **Generación de API Key en Weatherstack**
3. ✅ **Creación del Proyecto Python con Extracción de Datos**
4. ✅ **Cargue en GitHub**

---

## 📂 Estructura de Archivos

```
02-week/01-session/
├── etl-weatherstack-tutorial.html    ⭐ EMPIEZA AQUÍ
│   └─ Tutorial interactivo completo con los 4 pasos
├── extractor.py                      🐍 Script principal de ETL
├── etl_diagram.py                    📊 Generador de diagramas
├── requirements.txt                  📦 Dependencias Python
├── .env.example                      🔐 Ejemplo de configuración
└── README.md                         📖 Este archivo
```

---

## 🚀 Quick Start (5 minutos)

### 1. Abre el Tutorial HTML

```bash
# En Windows, abre con tu navegador:
explorer etl-weatherstack-tutorial.html

# O arrastra el archivo a tu navegador
```

### 2. Sigue los 4 Pasos Interactivos

El HTML contiene todo lo que necesitas saber en orden:

- 🖥️ **Fase 1**: Instalar WSL Ubuntu 24
- 🔑 **Fase 2**: Obtener API Key de Weatherstack
- 🐍 **Fase 3**: Crear proyecto Python
- 🚀 **Fase 4**: Subir a GitHub

### 3. Implementa el Código

Una vez hayas seguido el tutorial, aquí está el código listo para usar:

```bash
# Crear proyecto
mkdir mi-etl-weatherstack
cd mi-etl-weatherstack

# Clonar esqueleto (o copiar estos archivos)
# Instalar dependencias
pip install -r requirements.txt

# Configurar API Key
cp .env.example .env
# Edita .env y agrega tu API key de Weatherstack

# Ejecutar
python extractor.py
```

---

## 📋 Archivos en Detalle

### `etl-weatherstack-tutorial.html` (Principal) ⭐

**Qué es**: Tutorial interactivo completo en HTML

**Contiene**:
- Fase 1: Instalación de WSL Ubuntu 24 (8 pasos detallados)
- Fase 2: Generación de API Key Weatherstack (5 pasos)
- Fase 3: Proyecto Python completo (7 pasos + código)
- Fase 4: Cargue a GitHub (10 pasos + comandos)
- Diagrama visual del ETL
- Resumen y desafíos avanzados

**Cómo usar**:
```bash
# Abre en tu navegador
google-chrome etl-weatherstack-tutorial.html
firefox etl-weatherstack-tutorial.html
# O simplemente arrastra a la ventana del navegador
```

---

### `extractor.py` (Código Principal) 🐍

**Qué es**: Script Python que implementa todo el pipeline ETL

**Características**:
- ✅ Extrae datos de 5 ciudades desde Weatherstack
- ✅ Transforma y normaliza los datos
- ✅ Valida calidad de datos
- ✅ Manejo robusto de errores
- ✅ Logging detallado
- ✅ Guarda en CSV y JSON
- ✅ Muestra tabla resumen

**Uso**:
```bash
# Requiere variables en .env
python extractor.py

# Output esperado:
# ✅ Datos extraídos
# 💾 Archivos guardados (data/clima.csv, data/clima.json)
# 📊 Tabla mostrada en consola
# 🎨 Diagramas generados (si tienes etl_diagram.py)
```

**Clases**:
- `WeatherstackExtractor`: Clase principal que maneja todo el ETL
  - `__init__()`: Inicializa y valida configuración
  - `extraer_clima()`: Llamadas HTTP a la API
  - `procesar_respuesta()`: Normaliza el JSON en datos estructurados
  - `validar_datos()`: Valida rangos y campos obligatorios
  - `ejecutar_extraccion()`: Orquesta todo el proceso
  - `guardar_csv()`: Exporta a CSV
  - `guardar_json()`: Exporta a JSON
  - `mostrar_tabla()`: Imprime resumen en consola

---

### `etl_diagram.py` (Visualización) 📊

**Qué es**: Librería Python que genera diagramas visuales del ETL

**Genera 3 tipos de diagramas**:
1. **etl_flujo_principal.png** - Flujo general (Source → Extract → Transform → Load)
2. **etl_componentes.png** - Componentes del sistema (archivos, scripts, datos)
3. **etl_flujo_datos.png** - Transformación detallada de datos

**Uso**:
```bash
# Ejecutar directamente
python etl_diagram.py

# O desde otro script
from etl_diagram import DiagramaETL
diagrama = DiagramaETL()
diagrama.generar_todos_diagramas()
```

**Salida**: 
- `data/etl_flujo_principal.png`
- `data/etl_componentes.png`
- `data/etl_flujo_datos.png`

---

### `requirements.txt` 📦

**Qué es**: Lista de dependencias Python

**Contiene**:
```
requests==2.31.0          # Cliente HTTP
pandas==2.1.0             # Procesamiento de datos
python-dotenv==1.0.0      # Cargar variables de entorno
matplotlib==3.8.0         # Visualización
openpyxl==3.1.2           # Soporte Excel (opcional)
```

**Instalación**:
```bash
pip install -r requirements.txt
```

---

### `.env.example` 🔐

**Qué es**: Template de configuración (NO commitear el .env real)

**Contiene**:
```env
API_KEY=tu_api_key_aqui
WEATHERSTACK_BASE_URL=https://api.weatherstack.com
CIUDADES=Bogota,Medellin,Cali,Barranquilla,Cartagena
LOG_LEVEL=INFO
TIMEOUT=10
```

**Cómo usar**:
```bash
# Copiar el ejemplo
cp .env.example .env

# Editar con tu editor favorito
code .env
nano .env
vim .env

# Reemplazar: tu_api_key_aqui → tu clave real de Weatherstack
```

**⚠️ Seguridad**: 
- Nunca commitees `.env` a GitHub
- Agrega a `.gitignore`:
  ```
  .env
  .env.local
  .env*.local
  ```

---

## 🎯 Flujo Recomendado de Aprendizaje

### Día 1: Aprender Conceptos (30 min)
```
1. Lee la introducción del HTML (10 min)
2. Aprende sobre ETL y APIs (10 min)
3. Entiende la arquitectura (10 min)
```

### Día 2: Configurar Entorno (45 min)
```
1. Instala WSL Ubuntu 24 (Fase 1 del HTML) (20 min)
2. Configura VS Code Remote (10 min)
3. Instala Python y dependencias (15 min)
```

### Día 3: Obtener Credenciales (20 min)
```
1. Registrate en Weatherstack (Fase 2 HTML) (10 min)
2. Obtén tu API Key (5 min)
3. Configúralo en .env (5 min)
```

### Día 4: Implementar y Ejecutar (60 min)
```
1. Copia extractor.py a tu proyecto (2 min)
2. Ejecuta: python extractor.py (2 min)
3. Analiza los resultados (10 min)
4. Experimenta modificando ciudades (20 min)
5. Crea tus propios scripts basados en extractor.py (26 min)
```

### Día 5: Subir a GitHub (40 min)
```
1. Crea repositorio en GitHub (5 min)
2. Configura Git localmente (5 min)
3. Haz primeros commits (10 min)
4. Pushea a GitHub (5 min)
5. Escribe un buen README (10 min)
```

**Total: 3-4 horas de trabajo práctico**

---

## 📊 Datos Generados

Después de ejecutar `python extractor.py`, se crean:

### `data/clima.csv`
```csv
ciudad,pais,latitud,longitud,temperatura_c,humedad,velocidad_viento_kmh,descripcion,fecha_extraccion
Bogota,Colombia,4.71,-74.01,20,65,15.2,Partly cloudy,2026-02-11T14:30:45.123456
Medellin,Colombia,6.25,-75.57,24,70,8.5,Clear,2026-02-11T14:30:50.654321
```

### `data/clima.json`
```json
[
  {
    "ciudad": "Bogota",
    "pais": "Colombia",
    "temperatura_c": 20,
    "humedad": 65,
    "veloccion_viento_kmh": 15.2,
    "descripcion": "Partly cloudy",
    "fecha_extraccion": "2026-02-11T14:30:45.123456"
  },
  ...
]
```

### `logs/etl_YYYYMMDD_HHMMSS.log`
```
2026-02-11 14:30:40 - extractor - INFO - ✅ Configuración cargada
2026-02-11 14:30:41 - extractor - INFO - 📡 Extrayendo datos para: Bogota...
2026-02-11 14:30:42 - extractor - INFO - ✅ Datos extraídos para Bogota
```

---

## 🆘 Troubleshooting

### ❌ "API_KEY no configurada"
```
Solución:
1. Copia .env.example a .env
2. Edita .env y agrega tu API key real
3. Verifica sin espacios: API_KEY=a1b2c3d4...
```

### ❌ "No se obtienen datos"
```
Solución:
1. Verifica conexión a internet
2. Verifica que tu API key sea correcta
3. Comprueba en: https://weatherstack.com/dashboard
4. Verifica límite de solicitudes (plan Free: 250/mes)
```

### ❌ "ModuleNotFoundError: No module named 'requests'"
```
Solución:
pip install -r requirements.txt
```

### ❌ "Permission denied"
```
Solución (Linux/Mac):
chmod +x extractor.py
python extractor.py

O simplemente:
python3 extractor.py
```

---

## 🚀 Próximos Pasos (Desafíos)

### 🟢 Fácil
- [ ] Agregar más ciudades
- [ ] Cambiar formato de salida (JSON → XML)
- [ ] Agregar más campos de datos

### 🟡 Intermedio
- [ ] Automatizar con scheduler (ejecutar cada hora)
- [ ] Crear base de datos PostgreSQL local
- [ ] Agregar validaciones más estrictas

### 🔴 Avanzado
- [ ] Docker Compose con PostgreSQL
- [ ] API REST propia (FastAPI)
- [ ] Dashboard en Streamlit
- [ ] GitHub Actions para CI/CD

---

## 📚 Recursos Adicionales

- [Weatherstack API Docs](https://weatherstack.com/documentation)
- [Python Requests Docs](https://docs.python-requests.org/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Git & GitHub Tutorial](https://guides.github.com/)
- [WSL Official Docs](https://docs.microsoft.com/en-us/windows/wsl/)

---

## 📝 Licencia

Este material es de uso académico. CORHUILA - Ingeniería de Sistemas 2026.

---

## 🤝 Contribuciones

Si encuentras errores o tienes sugerencias:
1. Documenta el problema
2. Sugiere una solución
3. Contacta a tu profesor

---

## 📞 Soporte

- 💬 **Profesor**: Disponible en horario de clase
- 📧 **Email**: soporte@corhuila.edu.co
- 🌐 **Sitio Web**: https://www.corhuila.edu.co

---

**Última actualización**: 11 de Febrero, 2026  
**Versión**: 1.0  
**Estado**: ✅ Completo y funcional

✨ **¡Vamos a aprender Data Engineering!** ✨
