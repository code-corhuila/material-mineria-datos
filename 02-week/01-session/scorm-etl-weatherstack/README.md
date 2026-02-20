# 📦 Paquete SCORM - ETL Weatherstack para Moodle

Este es un paquete **SCORM 1.2** completamente funcional para cargar en **Moodle** o cualquier LMS compatible.

## 📋 Contenido del Paquete

```
scorm-etl-weatherstack/
├── imsmanifest.xml          ← Archivo principal de configuración SCORM
├── META-INF/                ← Metadatos SCORM
└── content/
    ├── index.html           ← Contenido principal (ETL Weatherstack)
    └── scorm.js             ← Script para integración con Moodle
```

## 🚀 Cómo Cargar en Moodle

### Método 1: Cargar como archivo ZIP (Recomendado)

1. **Comprimir la carpeta `scorm-etl-weatherstack`** como ZIP:
   - Haz clic derecho en `scorm-etl-weatherstack`
   - Selecciona "Enviar a" → "Carpeta comprimida"
   - Esto creará: `scorm-etl-weatherstack.zip`

2. **En Moodle**, ve al curso donde quieres añadir este contenido

3. **Habilita el Modo de Edición** (botón superior derecho)

4. **Añade una actividad SCORM**:
   - Haz clic en "Agregar una actividad o recurso"
   - Busca y selecciona **"SCORM"**
   - Configura:
     - **Nombre de la actividad**: "ETL Weatherstack - Minería de Datos"
     - **Descripción**: Copia la descripción a continuación
     - **Paquete SCORM**: Sube el archivo `scorm-etl-weatherstack.zip`
     - **Calificación**: SCORM (predeterminado)
     - **Intento automático**: Deshabilitado (o como prefieras)
   - Haz clic en **"Guardar y mostrar"**

5. **¡Listo!** El contenido estará disponible para los estudiantes

### Método 2: Cargar manualmente

Si tienes problemas con ZIP, puedes cargar directamente:

1. En Moodle, crea la actividad SCORM
2. Sea presenta con una opción para elegir el paquete
3. Descarga la carpeta completa `scorm-etl-weatherstack`
4. Sigue los pasos de tu LMS para cargar archivos individuales

## 📝 Descripción para Moodle

Copia y pega esta descripción en el campo de descripción de la actividad:

```
Aprende a crear un pipeline ETL profesional de principio a fin usando:
- WSL Ubuntu 24 en Windows
- Weatherstack API para datos de clima en tiempo real
- Python 3.11+ con librerías modernas
- Git y GitHub para versionamiento
- Visualización de datos con Matplotlib

El curso incluye 4 fases prácticas:
1. Alistamiento del entorno (WSL, Python, Git)
2. Generación de credenciales API
3. Desarrollo en Python (Extracción, Transformación, Carga)
4. Publicación en GitHub

Finaliza con preguntas de reflexión para socialización en grupo (16 parejas).

Tiempo estimado: 2 horas
Nivel: Intermedio-Avanzado
```

## ✅ Características de Rastreo SCORM

El paquete incluye rastreo automático de:

- ✓ **Inicio del curso**: Se registra cuando el estudiante abre la actividad
- ✓ **Progreso de lectura**: Se actualiza según desplazamiento por la página
- ✓ **Finalización**: Se marca como completada al llegar al final del contenido
- ✓ **Ubicación**: Se guarda la sección actual visitada

### Niveles de Progreso Automáticos

- 0% → Al abrir la actividad
- 50% → Al llegar a la mitad del contenido
- 80% → Al estar cerca del final
- 100% → Al alcanzar el final y marcar como completada

## 🔧 Especificaciones Técnicas

| Propiedad | Valor |
|-----------|-------|
| Versión SCORM | 1.2 |
| Tipo SCO | webcontent |
| Idioma | Español (es) |
| Formato | HTML5 + CSS3 + JavaScript |
| Tiempo típico | 2 horas (PT2H) |
| Dirigido a | Estudiantes de educación superior (18+) |
| Contexto | Ingeniería de Sistemas - Minería de Datos |

## 📱 Compatibilidad

✅ **Moodle** (versión 3.9+)  
✅ **Blackboard**  
✅ **Canvas**  
✅ **Schoology**  
✅ Cualquier LMS compatible con SCORM 1.2

## 🎯 Estándares de Completitud

La actividad se considera **completada** cuando:

1. El estudiante accede al contenido
2. Se desplaza hasta el final de la página
3. El script SCORM registra la finalización

**Nota**: Dependiendo de la configuración de Moodle, puede requerirse una calificación mínima.

## 📄 Archivos Incluidos

### imsmanifest.xml
Archivo de configuración SCORM que define:
- Metadatos del curso
- Estructura de navegación
- Recursos disponibles
- Objetivos de aprendizaje

### content/index.html
Contenido principal con:
- Tutorial completo sobre ETL
- Todas las fases del proyecto
- Código Python listo para usar
- Diagramas y visualizaciones
- Preguntas de reflexión para grupo

### content/scorm.js
Script que maneja:
- Comunicación con Moodle SCORM API
- Rastreo de progreso
- Manejo de errores
- Commit de datos

### META-INF/
Carpeta con metadatos adicionales SCORM

## ⚠️ Notas Importantes

1. **Asegúrate de mantener la estructura** de carpetas exactamente como está
2. **No renombres** los archivos principales (imsmanifest.xml, scorm.js)
3. **El archivo ZIP** debe contener la carpeta `scorm-etl-weatherstack` en su raíz
4. Si Moodle no reconoce el paquete, verifica que `imsmanifest.xml` esté en la raíz

## 🆘 Solución de Problemas

### Moodle no reconoce el paquete SCORM
- ✓ Verifica que imsmanifest.xml esté en la raíz
- ✓ Asegúrate el ZIP está bien formado
- ✓ Intenta descargar y re-comprimir sin la carpeta externa

### El contenido no muestra correctamente
- ✓ Verifica que index.html está en /content/
- ✓ Las imágenes externas (de URLs) deben ser accesibles
- ✓ Chrome/Firefox/Edge tienen mejor soporte que Explorer

### El rastreo no funciona
- ✓ Asegúrate que JavaScript está habilitado en el navegador
- ✓ Verifica que scorm.js está en /content/
- ✓ Espera 5 segundos después de abrir antes de cerrar

## 👨‍🏫 Para Instructores

Este SCORM está diseñado para:

- **Clases presenciales**: Usarlo como material de referencia complementario
- **Educación a distancia**: Como contenido principal con actividades adicionales
- **Aprendizaje híbrido**: Combinarlo con foros, tareas y quizes en Moodle

Se recomienda:
1. Asignar esta actividad como lectura previa
2. Realizar actividades prácticas después
3. Usar foros para discusiones
4. Evaluar con proyectos o exámenes adicionales

## 🔐 Derechos de Autor

© 2026 **CORHUILA - Corporación Universitaria de Huila**
Ingeniería de Sistemas | Minería de Datos

**Uso autorizado**: Educativo institucional  
**Contacto**: [Datos de contacto CORHUILA]

---

## 📞 Soporte

Para problemas con el SCORM:
- Contacta al departamento de TI de tu Moodle
- Verifica la compatibilidad de tu versión SCORM
- Consulta la documentación de tu LMS

Para problemas con el contenido:
- Revisa el material HTML directamente en un navegador
- Verifica los enlaces externos (Weatherstack API, GitHub, etc.)
- Contacta al autor: **Ing. Julian Quimbayo Castro**

---

**Última actualización**: 13 de febrero de 2026  
**Versión SCORM**: 1.0  
**Estado**: Completo y listo para producción ✅
