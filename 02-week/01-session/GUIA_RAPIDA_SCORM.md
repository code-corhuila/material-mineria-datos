# 🚀 Guía Rápida - Cargar SCORM a Moodle

## ✅ TodooListo!

Tu paquete SCORM está **completamente configurado y listo** para cargar a Moodle.

## 📦 Archivos Generados

```
📂 material-mineria-datos/02-week/01-session/
├── scorm-etl-weatherstack.zip          ← ⭐ SUBE ESTE ARCHIVO A MOODLE
└── scorm-etl-weatherstack/             (carpeta original - para ediciones)
    ├── imsmanifest.xml
    ├── README.md
    ├── compress-scorm.bat
    ├── META-INF/metadata.xml
    └── content/
        ├── index.html
        └── scorm.js
```

## 🎯 Pasos Rápidos para Moodle

### 1️⃣ **Descarga el ZIP**
   - Ubicación: `scorm-etl-weatherstack.zip`
   - Tamaño: ~20 KB (muy pequeño y rápido)

### 2️⃣ **En Moodle - Crear Actividad**
   ```
   Curso → Modo de Edición ON → "Agregar actividad o recurso" 
   → Buscar "SCORM" → Agregar
   ```

### 3️⃣ **Configurar SCORM**
   | Campo | Valor |
   |-------|-------|
   | Nombre | ETL Weatherstack - Minería de Datos |
   | Descripción | (Ver archivo README.md) |
   | Paquete SCORM | Subir `scorm-etl-weatherstack.zip` |
   | Otros | Dejar valores por defecto |

### 4️⃣ **Guardar**
   - Haz clic en "Guardar y mostrar"
   - ¡Listo! Los estudiantes pueden acceder

---

## 🔧 Especificaciones SCORM

| Aspecto | Detalles |
|---------|----------|
| **Versión** | SCORM 1.2 (compatible universal) |
| **Tamaño ZIP** | ~20 KB |
| **Contenido** | HTML5 + CSS3 + JavaScript |
| **Rastreo** | Automático (progreso, finalización) |
| **Compatibilidad** | Moodle, Canvas, Blackboard, Schoology |

---

## ✨ Características Incluidas

✅ **Rastreo automático**
   - Se marca automáticamente cuando el estudiante llega al final
   - Progreso se actualiza al desplazarse

✅ **Navegación interactiva**
   - Menú fijo con links a cada sección
   - Botón para ir al inicio en cualquier momento
   - Copiar código con un clic

✅ **Diseño responsivo**
   - Se adapta a móviles, tablets y laptops
   - Compatible con todos los navegadores modernos

✅ **Contenido completo**
   - 4 fases prácticas del ETL
   - Código Python listo para usar
   - 16 preguntas de reflexión para grupo

---

## 📱 Navegadores Soportados

| Navegador | Versión Mínima | Estado |
|-----------|---|---|
| Chrome | 70+ | ✅ Excelente |
| Firefox | 65+ | ✅ Excelente |
| Safari | 12+ | ✅ Bueno |
| Edge | 79+ | ✅ Excelente |
| Internet Explorer | 11 | ⚠️ Limitado |

---

## 🎓 Para Instructores

### Configuración Recomendada en Moodle:

1. **Calificación**: "SCORM" (predeterminado)
2. **Intento automático**: "Deshabilitado" (permite múltiples réplicas)
3. **Mostrar resumen de intentos**: "Cuando el intento es finalizado"
4. **Grado de aprobación**: Depende de tu política (sugerido: 50%)

### Instrucciones para Estudiantes:

> _"Esta actividad ETL Weatherstack es un tutorial interactivo que debes completar antes de la sesión práctica._
>
> _Léelo completamente (aprox. 45-60 min) y responde las preguntas de reflexión en grupo. Se registrará automáticamente tu progreso en Moodle."_

---

## ⚠️ Verificación Antes de Subir

✓ Archivo ZIP existe: `scorm-etl-weatherstack.zip`  
✓ Tamaño razonable: ~20 KB  
✓ imsmanifest.xml está presente  
✓ Contenido HTML accesible  
✓ Scripts de SCORM incluidos  

---

## 🆘 Si Hay Problemas

### **Moodle no reconoce el SCORM**
```
Solución: Asegúrate que:
- El ZIP está bien formado
- imsmanifest.xml está en la raíz (no en subfarpeta)
- Intenta descomprimir y re-comprimir
```

### **El contenido no se muestra**
```
Solución:
- Limpia caché del navegador (Ctrl+Shift+Del)
- Intenta en otro navegador
- Verifica que JavaScript está habilitado
```

### **No hay progreso registrado**
```
Solución:
- Espera 10 segundos después de abrir
- Navega hasta el final de la página
- Cierra y reabre la actividad
```

---

## 📚 Documentación Adicional

Para más detalles, consulta:
- **README.md** en la carpeta `scorm-etl-weatherstack/`
- **imsmanifest.xml** (configuración SCORM)
- **content/index.html** (contenido completo)

---

## 🔄 Si Necesitas Editar el Contenido

1. Edita el archivo `scorm-etl-weatherstack/content/index.html`
2. Haz los cambios necesarios
3. Ejecuta `compress-scorm.bat` para regenerar el ZIP
4. Sube el nuevo ZIP a Moodle (reemplaza el anterior)

---

## 📞 Soporte Técnico

- **Problemas SCORM/Moodle**: Tu equipo de TI
- **Contenido/Ejercicios**: Ing. Julian Quimbayo Castro
- **Errores en la plataforma**: System administrator

---

## 🎉 ¡LISTO!

Tu paquete SCORM está 100% operativo y listo para producción.

**Próximo paso**: Carga el archivo ZIP a Moodle y verifica que aparezca correctamente.

---

**Fecha de creación**: 13 febrero 2026  
**Versión SCORM**: 1.2  
**Estado**: Producción ✅  
**Autor**: Ing. Julian Quimbayo Castro - CORHUILA
