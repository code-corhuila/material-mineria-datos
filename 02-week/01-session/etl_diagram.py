#!/usr/bin/env python3
"""
Módulo para visualizar la arquitectura del pipeline ETL Weatherstack
Genera diagramas de flujo del proceso de extracción, transformación y carga de datos
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
from pathlib import Path

class DiagramaETL:
    """Genera visualizaciones de la arquitectura del ETL"""
    
    def __init__(self, output_dir='data'):
        """
        Inicializa el generador de diagramas
        
        Args:
            output_dir (str): Directorio donde guardar las imágenes
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
        # Colores
        self.color_extract = '#FF6B6B'
        self.color_transform = '#4ECDC4'
        self.color_load = '#95E1D3'
        self.color_data = '#FFE66D'
        self.color_api = '#A8E6CF'
    
    def dibujar_caja(self, ax, x, y, ancho, alto, texto, color, fontsize=10):
        """Dibuja una caja redondeada con texto"""
        box = FancyBboxPatch(
            (x - ancho/2, y - alto/2), ancho, alto,
            boxstyle="round,pad=0.1",
            edgecolor='black', facecolor=color,
            linewidth=2, alpha=0.8
        )
        ax.add_patch(box)
        ax.text(x, y, texto, ha='center', va='center',
                fontsize=fontsize, fontweight='bold',
                wrap=True)
    
    def dibujar_flecha(self, ax, x1, y1, x2, y2, etiqueta=''):
        """Dibuja una flecha entre dos puntos"""
        arrow = FancyArrowPatch(
            (x1, y1), (x2, y2),
            arrowstyle='->', mutation_scale=30,
            linewidth=2.5, color='#333333'
        )
        ax.add_patch(arrow)
        
        # Etiqueta de la flecha
        if etiqueta:
            mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
            ax.text(mid_x + 0.3, mid_y + 0.3, etiqueta,
                   fontsize=8, style='italic',
                   bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    def diagrama_flujo_principal(self):
        """Crea el diagrama de flujo principal del ETL"""
        fig, ax = plt.subplots(1, 1, figsize=(14, 10))
        
        # Configurar ejes
        ax.set_xlim(-0.5, 10)
        ax.set_ylim(-0.5, 10)
        ax.axis('off')
        
        # Título
        ax.text(5, 9.5, 'ARQUITECTURA DEL PIPELINE ETL - WEATHERSTACK',
               fontsize=16, fontweight='bold', ha='center')
        ax.text(5, 9, 'Extracción → Transformación → Carga → Análisis',
               fontsize=11, ha='center', style='italic', color='#555')
        
        # LAYER 1: ORIGEN DE DATOS
        self.dibujar_caja(ax, 5, 7.8, 2, 0.8, 
                         'Weatherstack API\n(Datos de Clima)',
                         self.color_api, fontsize=9)
        
        # Flecha 1
        self.dibujar_flecha(ax, 5, 7.4, 5, 6.8, '')
        
        # LAYER 2: EXTRACCIÓN
        self.dibujar_caja(ax, 5, 6.2, 2.5, 0.8,
                         '📥 EXTRACT\nextractor.py',
                         self.color_extract, fontsize=9)
        
        # Proceso detallado de extracción
        ax.text(0.5, 5.5, 'Proceso:',
               fontsize=9, fontweight='bold')
        ax.text(0.5, 5.1, '• Conectar a API', fontsize=8)
        ax.text(0.5, 4.7, '• 5 ciudades', fontsize=8)
        ax.text(0.5, 4.3, '• Validar', fontsize=8)
        ax.text(0.5, 3.9, '• Logging', fontsize=8)
        
        # Flecha 2
        self.dibujar_flecha(ax, 5, 5.8, 5, 5.2, '')
        
        # LAYER 3: TRANSFORMACIÓN
        self.dibujar_caja(ax, 5, 4.6, 2.5, 0.8,
                         '⚙️ TRANSFORM\nprocesar_respuesta()',
                         self.color_transform, fontsize=9)
        
        # Proceso detallado de transformación
        ax.text(9.2, 5.5, 'Proceso:',
               fontsize=9, fontweight='bold')
        ax.text(9.2, 5.1, '• Normalizar', fontsize=8)
        ax.text(9.2, 4.7, '• Limpiar', fontsize=8)
        ax.text(9.2, 4.3, '• Enriquecer', fontsize=8)
        ax.text(9.2, 3.9, '• Validar tipos', fontsize=8)
        
        # Flecha 3
        self.dibujar_flecha(ax, 5, 4.2, 5, 3.6, '')
        
        # LAYER 4: CARGA/ALMACENAMIENTO
        self.dibujar_caja(ax, 5, 3, 2.5, 0.8,
                         '💾 LOAD\nGuardar datos',
                         self.color_load, fontsize=9)
        
        # Tres salidas paralelas
        ax.text(0.3, 2.2, 'CSV', fontsize=8, fontweight='bold',
               bbox=dict(boxstyle='round', facecolor=self.color_data, alpha=0.7))
        ax.text(5, 2.2, 'JSON', fontsize=8, fontweight='bold',
               bbox=dict(boxstyle='round', facecolor=self.color_data, alpha=0.7))
        ax.text(9.7, 2.2, 'PNG', fontsize=8, fontweight='bold',
               bbox=dict(boxstyle='round', facecolor=self.color_data, alpha=0.7))
        
        # Flechas hacia salidas
        self.dibujar_flecha(ax, 3.5, 2.6, 0.3, 1.8, 'clima.csv')
        self.dibujar_flecha(ax, 5, 2.6, 5, 1.8, 'clima_raw.json')
        self.dibujar_flecha(ax, 6.5, 2.6, 9.7, 1.8, 'análisis.png')
        
        # LAYER 5: RESULTADO
        ax.text(5, 0.8, '✅ DATOS LISTOS PARA ANÁLISIS Y BI',
               fontsize=11, fontweight='bold', ha='center',
               bbox=dict(boxstyle='round', facecolor='#C8E6C9', 
                        edgecolor='#27AE60', linewidth=2))
        
        # Leyenda de duración
        ax.text(0.5, 0.2, '⏱️ Duración: ~2-5 segundos por ejecución',
               fontsize=8, style='italic')
        ax.text(5, 0.2, '📊 Volumen: ~100-200 registros',
               fontsize=8, style='italic')
        ax.text(9.2, 0.2, '🔄 Frecuencia: Manual',
               fontsize=8, style='italic')
        
        plt.tight_layout()
        output_file = self.output_dir / 'etl_flujo_principal.png'
        plt.savefig(output_file, dpi=300, bbox_inches='tight', facecolor='white')
        print(f"✅ Diagrama guardado: {output_file}")
        plt.close()
    
    def diagrama_componentes(self):
        """Crea un diagrama de componentes del sistema"""
        fig, ax = plt.subplots(1, 1, figsize=(14, 10))
        
        ax.set_xlim(-0.5, 10)
        ax.set_ylim(-0.5, 10)
        ax.axis('off')
        
        # Título
        ax.text(5, 9.5, 'COMPONENTES DEL SISTEMA ETL',
               fontsize=16, fontweight='bold', ha='center')
        
        # CONFIGURACIÓN
        self.dibujar_caja(ax, 2, 8, 1.8, 0.8, '.env\nVariables',
                         '#FFE66D', fontsize=9)
        
        # FUENTE DE DATOS
        self.dibujar_caja(ax, 5, 8, 1.8, 0.8, 'API\nWeatherstack',
                         '#A8E6CF', fontsize=9)
        
        # SEGURIDAD
        self.dibujar_caja(ax, 8, 8, 1.8, 0.8, '🔒 Seguridad\nAPI Key',
                         '#FF9999', fontsize=9)
        
        # EXTRACTOR
        self.dibujar_caja(ax, 2, 6, 1.8, 0.8, 'extractor.py\nClase Principal',
                         self.color_extract, fontsize=9)
        
        # PROCESADOR
        self.dibujar_caja(ax, 5, 6, 1.8, 0.8, 'procesar()\nNormalización',
                         self.color_transform, fontsize=9)
        
        # LOGGER
        self.dibujar_caja(ax, 8, 6, 1.8, 0.8, 'logging\nRegistros',
                         '#B3E5FC', fontsize=9)
        
        # ALMACENAMIENTO
        self.dibujar_caja(ax, 1.5, 4, 1.5, 0.8, 'CSV\nTabular',
                         self.color_data, fontsize=9)
        self.dibujar_caja(ax, 3.5, 4, 1.5, 0.8, 'JSON\nEstructurado',
                         self.color_data, fontsize=9)
        self.dibujar_caja(ax, 5.5, 4, 1.5, 0.8, 'PNG\nGráficas',
                         self.color_data, fontsize=9)
        self.dibujar_caja(ax, 7.5, 4, 1.5, 0.8, 'LOG\nRegistros',
                         '#FFCCBC', fontsize=9)
        
        # VERSIONAMIENTO
        self.dibujar_caja(ax, 5, 2, 2, 0.8, 'Git/GitHub\nControl de Versiones',
                         '#E1BEE7', fontsize=9)
        
        # ANÁLISIS
        self.dibujar_caja(ax, 5, 0.5, 2.5, 0.8, '📊 Pandas + Matplotlib\nAnálisis y Visualización',
                         '#C8E6C9', fontsize=9)
        
        # Flechas de flujo
        self.dibujar_flecha(ax, 2, 7.6, 2, 6.4)  # Config a extractor
        self.dibujar_flecha(ax, 5, 7.6, 5, 6.4)  # API a procesador
        self.dibujar_flecha(ax, 8, 7.6, 8, 6.4)  # Seguridad a logger
        
        # Flechas de salida
        self.dibujar_flecha(ax, 2, 5.6, 1.5, 4.4)
        self.dibujar_flecha(ax, 5, 5.6, 3.5, 4.4)
        self.dibujar_flecha(ax, 5, 5.6, 5.5, 4.4)
        self.dibujar_flecha(ax, 8, 5.6, 7.5, 4.4)
        
        # Flechas hacia Git
        self.dibujar_flecha(ax, 1.5, 3.6, 4.5, 2.4)
        self.dibujar_flecha(ax, 7.5, 3.6, 5.5, 2.4)
        
        # Flecha hacia análisis
        self.dibujar_flecha(ax, 5, 1.6, 5, 0.9)
        
        plt.tight_layout()
        output_file = self.output_dir / 'etl_componentes.png'
        plt.savefig(output_file, dpi=300, bbox_inches='tight', facecolor='white')
        print(f"✅ Diagrama guardado: {output_file}")
        plt.close()
    
    def diagrama_flujo_datos(self):
        """Crea un diagrama detallado del flujo de datos"""
        fig, ax = plt.subplots(1, 1, figsize=(14, 10))
        
        ax.set_xlim(-0.5, 10)
        ax.set_ylim(-0.5, 10)
        ax.axis('off')
        
        # Título
        ax.text(5, 9.5, 'FLUJO DE DATOS DETALLADO',
               fontsize=16, fontweight='bold', ha='center')
        
        # Etapa 1: API Response
        ax.text(1.5, 8.8, 'ETAPA 1: API Response', fontsize=9, fontweight='bold')
        ax.text(1.5, 8.3, 'Formato JSON:\n{',
               fontsize=8, family='monospace',
               bbox=dict(boxstyle='round', facecolor='#FFE66D', alpha=0.7))
        ax.text(1.5, 7.6, '"current": {...},\n"location": {...}', fontsize=7,
               family='monospace')
        
        # Flecha
        self.dibujar_flecha(ax, 2, 7.2, 5, 6.8)
        
        # Etapa 2: Extracción
        ax.text(5.5, 8.8, 'ETAPA 2: Extracción', fontsize=9, fontweight='bold')
        ax.text(5.5, 8.3, 'Campos relevantes:\n- temperatura\n- humedad\n- ciudad\n- timestamp',
               fontsize=8)
        
        # Flecha
        self.dibujar_flecha(ax, 5, 7.2, 8, 6.8)
        
        # Etapa 3: Normalización
        ax.text(8.5, 8.8, 'ETAPA 3: Normalizado', fontsize=9, fontweight='bold')
        ax.text(8.5, 8.3, 'Tipos consistentes:\n- Números\n- Strings\n- Timestamps',
               fontsize=8)
        
        # Salida CSV
        ax.text(1, 5.5, 'CSV (Tabular)', fontsize=10, fontweight='bold',
               bbox=dict(boxstyle='round', facecolor=self.color_data, alpha=0.8))
        ax.text(1, 5, 'ciudad,temp,humedad\nBogota,22,65\nMedellin,24,70',
               fontsize=7, family='monospace',
               bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
        
        # Salida JSON
        ax.text(5, 5.5, 'JSON (Estructurado)', fontsize=10, fontweight='bold',
               bbox=dict(boxstyle='round', facecolor=self.color_data, alpha=0.8))
        ax.text(5, 5, '[{\n  "ciudad":"Bogota",\n  "temp":22\n}]',
               fontsize=7, family='monospace',
               bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
        
        # Salida PNG
        ax.text(9, 5.5, 'PNG (Visualizado)', fontsize=10, fontweight='bold',
               bbox=dict(boxstyle='round', facecolor=self.color_data, alpha=0.8))
        ax.text(8.3, 4.7, '📊\n[Gráficos]', fontsize=9,
               bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
        
        # Flechas hacia salidas
        self.dibujar_flecha(ax, 5, 6.2, 1, 5.9)
        self.dibujar_flecha(ax, 5, 6.2, 5, 5.9)
        self.dibujar_flecha(ax, 5, 6.2, 9, 5.9)
        
        # Estadísticas
        stats_y = 3
        ax.text(2, stats_y + 1, '📊 ESTADÍSTICAS', fontsize=10, fontweight='bold')
        stats = [
            '• Ciudades: 5',
            '• Campos por ciudad: 10',
            '• Registros por ejecución: ~5',
            '• Tamaño CSV: ~2-5 KB',
            '• Tamaño JSON: ~3-8 KB',
        ]
        for i, stat in enumerate(stats):
            ax.text(2, stats_y - i*0.35, stat, fontsize=8)
        
        # Quality Checks
        ax.text(5.5, stats_y + 1, '✅ CALIDAD DE DATOS', fontsize=10, fontweight='bold')
        checks = [
            '✓ Sin valores nulos',
            '✓ Tipos consistentes',
            '✓ Rangos válidos',
            '✓ Timestamps consistentes',
            '✓ Duplicados detectados',
        ]
        for i, check in enumerate(checks):
            ax.text(5.5, stats_y - i*0.35, check, fontsize=8, color='#27AE60')
        
        # Performance
        ax.text(8, stats_y + 1, '⚡ PERFORMANCE', fontsize=10, fontweight='bold')
        perf = [
            '• Tiempo API: ~800ms',
            '• Transformación: ~50ms',
            '• Escritura: ~100ms',
            '• Total: ~2-3 seg',
            '• Throughput: ~2.5 rec/seg',
        ]
        for i, p in enumerate(perf):
            ax.text(8, stats_y - i*0.35, p, fontsize=8)
        
        # Footer
        ax.text(5, 0.2, '🔄 Este flujo se repite cada ejecución del script extractor.py',
               fontsize=9, style='italic', ha='center')
        
        plt.tight_layout()
        output_file = self.output_dir / 'etl_flujo_datos.png'
        plt.savefig(output_file, dpi=300, bbox_inches='tight', facecolor='white')
        print(f"✅ Diagrama guardado: {output_file}")
        plt.close()
    
    def generar_todos_diagramas(self):
        """Genera todos los diagramas"""
        print("\n" + "="*60)
        print("GENERANDO DIAGRAMAS DEL PIPELINE ETL")
        print("="*60)
        
        print("\n1️⃣  Generando diagrama de flujo principal...")
        self.diagrama_flujo_principal()
        
        print("\n2️⃣  Generando diagrama de componentes...")
        self.diagrama_componentes()
        
        print("\n3️⃣  Generando diagrama de flujo de datos...")
        self.diagrama_flujo_datos()
        
        print("\n" + "="*60)
        print("✅ TODOS LOS DIAGRAMAS GENERADOS EXITOSAMENTE")
        print("="*60)
        print(f"\n📁 Ubicación: {self.output_dir.absolute()}/")
        print("\nArchivos generados:")
        print("  • etl_flujo_principal.png - Flujo general del ETL")
        print("  • etl_componentes.png - Componentes del sistema")
        print("  • etl_flujo_datos.png - Transformación de datos")


if __name__ == "__main__":
    # Ejecutable directo
    generador = DiagramaETL(output_dir='data')
    generador.generar_todos_diagramas()
    
    print("\n💡 Para usar en tu proyecto:")
    print("   from etl_diagram import DiagramaETL")
    print("   diagrama = DiagramaETL()")
    print("   diagrama.generar_todos_diagramas()")
