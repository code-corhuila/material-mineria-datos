# Paquete SCORM: 15 Proyectos ETL, Dashboard y Machine Learning

## Descripción

Este es un paquete SCORM 1.2 que contiene un completo curso sobre:
- Pipelines ETL (Extracción, Transformación, Carga)
- Visualización de datos con Streamlit
- Machine Learning y análisis predictivo
- Containerización con Docker
- 15 proyectos prácticos con APIs públicas

## Contenido del paquete

```
scorm-proyectos/
├── imsmanifest.xml      (Archivo de manifiesto SCORM - NO MODIFICAR)
├── index.html           (Contenido principal del curso)
├── css/
│   └── styles.css       (Estilos CSS)
├── js/
│   └── scripts.js       (Funcionalidad JavaScript)
└── assets/
    └── logo-corhuila.png (Logo de la institución)
```

## Instalación en Moodle

### Paso 1: Preparar el archivo ZIP

1. **Descargue el logo** (opcional):
   - Descargue el logo de Corhuila desde:
     https://raw.githubusercontent.com/code-corhuila/material-mineria-datos/b3725d694125ab35294ddfe415a327bc1445d32c/01-week/01-session/LOGO%20CORHUILA%20BLANCO%20PNG%20(2).png
   - Guárdelo en la carpeta `assets/` como `logo-corhuila.png`

2. **Comprimir la carpeta**:
   - Haga clic derecho en la carpeta `scorm-proyectos/`
   - Seleccione "Enviar a" → "Carpeta comprimida"
   - O use 7-Zip, WinRAR, etc.
   - El archivo resultante será: `scorm-proyectos.zip`

### Paso 2: Subir a Moodle

1. **Acceda a su curso en Moodle**
2. **Active el modo de edición** (botón "Activar edición" en la esquina superior derecha)
3. **Agregue una actividad SCORM**:
   - Haga clic en "Agregar una actividad o un recurso"
   - Seleccione "SCORM/AICC"
   - Clic en "Agregar"
4. **Configure la actividad**:
   - **Nombre**: "15 Proyectos ETL, Dashboard y ML"
   - **Descripción**: (Opcional) Describa el curso
   - **Paquete SCORM**: Clic en "Elegir archivo" → Seleccione `scorm-proyectos.zip`
5. **Guarde cambios**

### Paso 3: Verificación

1. Visualice el curso desde la perspectiva de un estudiante
2. Haga clic en la actividad SCORM
3. Verifique que el contenido se cargue correctamente
4. Pruebe la navegación y los acordeones de proyectos

## Características

✅ **15 Proyectos completos** con descripciones, APIs y entregables  
✅ **Acordeones interactivos** para expandir/contraer proyectos  
✅ **Rúbrica de evaluación** con escala institucional colombiana  
✅ **Responsive design** - Compatible con móviles y tablets  
✅ **Sin dependencias externas** - Todo incluido en el paquete  
✅ **Fácil de personalizar** - Edite los archivos HTML, CSS, JS según necesite  

## Personalizaciones

### Cambiar el logo
Edite `index.html` línea con `<img src="assets/logo-corhuila.png"` para usar su propio logo.

### Modificar colores
Edite `css/styles.css` y cambie las variables CSS:
```css
:root {
    --primary-color: #1e3c72;        /* Azul primario */
    --secondary-color: #2a5298;      /* Azul secundario */
    --accent-color: #ff6b6b;         /* Rojo acentuado */
}
```

### Agregar/Modificar proyectos
Edite `index.html` y busque `<!-- Proyecto X -->` para modificar el contenido.

## Compatibilidad

- ✅ Moodle 3.9+ (Tested en 4.0, 4.1)
- ✅ SCORM 1.2
- ✅ Navegadores modernos (Chrome, Firefox, Safari, Edge)
- ✅ Dispositivos móviles (responsive)

## Notas importantes

1. **Logo roto**: Si el logo no aparece, descargue e incluya el archivo `logo-corhuila.png` en la carpeta `assets/`
2. **Estilos no aplican**: Limpie el caché del navegador (Ctrl+Shift+Delete)
3. **Acordeones no funcionan**: Verifique que JavaScript esté habilitado en el navegador

## Soporte

Para problemas con el contenido o la visualización:
1. Verifique que todos los archivos estén en el ZIP
2. Compruebe que el archivo imsmanifest.xml no ha sido modificado
3. Asegúrese de que Moodle tiene habilitado JavaScript

## Autor

Creado por: **Ing. Julian Andres Quimbayo Castro**  
Institución: **Corhuila - Ingeniería de Sistemas**  
Año: **2025**

---

**Versión**: 1.0  
**Última actualización**: Febrero 2025
