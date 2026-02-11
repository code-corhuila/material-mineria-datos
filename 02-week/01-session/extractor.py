#!/usr/bin/env python3
"""
Extractor ETL para Weatherstack API
Módulo principal de extracción de datos de clima

Uso:
    python extractor.py

Requiere:
    - requests
    - pandas
    - python-dotenv
"""

import os
import requests
import json
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
import logging
from typing import Optional, Dict, List, Any

# ============================================================================
# CONFIGURACIÓN DE LOGGING
# ============================================================================

def configurar_logging(log_dir: str = 'logs') -> logging.Logger:
    """
    Configura logging para la aplicación
    
    Args:
        log_dir: Directorio para guardar logs
        
    Returns:
        Logger configurado
    """
    # Crear directorio si no existe
    os.makedirs(log_dir, exist_ok=True)
    
    # Nombre del archivo log
    log_file = os.path.join(log_dir, f"etl_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")
    
    # Configurar logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    
    logger = logging.getLogger(__name__)
    logger.info("=" * 70)
    logger.info("INICIANDO PIPELINE ETL WEATHERSTACK")
    logger.info("=" * 70)
    
    return logger


logger = configurar_logging()


# ============================================================================
# CLASE PRINCIPAL: WEATHERSTACK EXTRACTOR
# ============================================================================

class WeatherstackExtractor:
    """
    Extrae datos de clima desde Weatherstack API
    
    Attributes:
        api_key (str): Clave de acceso a la API
        base_url (str): URL base de la API
        ciudades (List[str]): Lista de ciudades a consultar
        timeout (int): Tiempo máximo de espera en segundos
    """
    
    def __init__(self, timeout: int = 10):
        """
        Inicializa el extractor
        
        Args:
            timeout: Tiempo máximo de espera para solicitudes HTTP
            
        Raises:
            ValueError: Si no encuentra API_KEY en variables de entorno
        """
        # Cargar variables de entorno
        load_dotenv()
        
        self.api_key = os.getenv('API_KEY')
        self.base_url = os.getenv('WEATHERSTACK_BASE_URL', 'https://api.weatherstack.com')
        ciudades_env = os.getenv('CIUDADES', 'Bogota,Medellin,Cali,Barranquilla,Cartagena')
        self.ciudades = [c.strip() for c in ciudades_env.split(',')]
        self.timeout = timeout
        
        # Validar configuración
        if not self.api_key:
            raise ValueError("❌ API_KEY no configurada en archivo .env")
        
        logger.info(f"✅ Configuración cargada:")
        logger.info(f"   - Base URL: {self.base_url}")
        logger.info(f"   - Ciudades: {', '.join(self.ciudades)}")
        logger.info(f"   - Timeout: {self.timeout}s")
    
    def extraer_clima(self, ciudad: str) -> Optional[Dict[str, Any]]:
        """
        Extrae datos de clima para una ciudad específica
        
        Args:
            ciudad: Nombre de la ciudad
            
        Returns:
            Dict con respuesta JSON o None si hay error
        """
        try:
            # Preparar solicitud
            url = f"{self.base_url}/current"
            params = {
                'access_key': self.api_key,
                'query': ciudad.strip()
            }
            
            logger.info(f"📡 Extrayendo datos para: {ciudad}...")
            
            # Realizar solicitud
            response = requests.get(url, params=params, timeout=self.timeout)
            response.raise_for_status()  # Lanza excepción si HTTP error
            
            # Parsear JSON
            data = response.json()
            
            # Verificar si hay errores en la respuesta
            if 'error' in data:
                error_msg = data['error'].get('info', 'Error desconocido')
                logger.error(f"❌ Error API para {ciudad}: {error_msg}")
                return None
            
            # Validar que tenga datos
            if 'current' not in data or 'location' not in data:
                logger.warning(f"⚠️  Respuesta incompleta para {ciudad}")
                return None
            
            logger.info(f"✅ Datos extraídos correctamente para {ciudad}")
            return data
            
        except requests.exceptions.Timeout:
            logger.error(f"❌ Timeout para {ciudad} (>{self.timeout}s)")
        except requests.exceptions.ConnectionError:
            logger.error(f"❌ Error de conexión para {ciudad}")
        except requests.exceptions.RequestException as e:
            logger.error(f"❌ Error HTTP para {ciudad}: {str(e)}")
        except json.JSONDecodeError:
            logger.error(f"❌ Respuesta JSON inválida para {ciudad}")
        except Exception as e:
            logger.error(f"❌ Error inesperado para {ciudad}: {str(e)}")
        
        return None
    
    def procesar_respuesta(self, response_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        Procesa la respuesta JSON a formato estructurado
        
        Args:
            response_data: Respuesta JSON de la API
            
        Returns:
            Dict con datos procesados o None si hay error
        """
        try:
            current = response_data.get('current', {})
            location = response_data.get('location', {})
            
            # Extraer datos
            datos_procesados = {
                'ciudad': location.get('name', 'N/A'),
                'pais': location.get('country', 'N/A'),
                'latitud': float(location.get('lat', 0)) if location.get('lat') else None,
                'longitud': float(location.get('lon', 0)) if location.get('lon') else None,
                'temperatura_c': float(current.get('temperature', 0)) if current.get('temperature') else None,
                'temperatura_f': float(current.get('temperature', 0)) * 9/5 + 32 if current.get('temperature') else None,
                'sensacion_termica': float(current.get('feelslike', 0)) if current.get('feelslike') else None,
                'humedad': int(current.get('humidity', 0)) if current.get('humidity') else None,
                'velocidad_viento_kmh': float(current.get('wind_speed', 0)) if current.get('wind_speed') else None,
                'presion': int(current.get('pressure', 0)) if current.get('pressure') else None,
                'descripcion': current.get('weather_descriptions', ['N/A'])[0] if current.get('weather_descriptions') else 'N/A',
                'codigo_clima': int(current.get('weather_code', 0)) if current.get('weather_code') else None,
                'fecha_extraccion': datetime.now().isoformat(),
                'zona_horaria': location.get('timezone_id', 'N/A')
            }
            
            return datos_procesados
            
        except (KeyError, ValueError, TypeError) as e:
            logger.error(f"❌ Error procesando respuesta: {str(e)}")
            return None
    
    def validar_datos(self, datos: Dict[str, Any]) -> bool:
        """
        Valida que los datos tengan formato correcto
        
        Args:
            datos: Datos a validar
            
        Returns:
            True si los datos son válidos, False en caso contrario
        """
        try:
            # Campos obligatorios
            campos_obligatorios = ['ciudad', 'temperatura_c', 'humedad', 'fecha_extraccion']
            for campo in campos_obligatorios:
                if campo not in datos or datos[campo] is None:
                    logger.warning(f"⚠️  Campo obligatorio faltante: {campo}")
                    return False
            
            # Validar rangos razonables
            temp = datos.get('temperatura_c')
            if temp is not None and (temp < -50 or temp > 60):
                logger.warning(f"⚠️  Temperatura fuera de rango: {temp}°C")
                return False
            
            humedad = datos.get('humedad')
            if humedad is not None and (humedad < 0 or humedad > 100):
                logger.warning(f"⚠️  Humedad fuera de rango: {humedad}%")
                return False
            
            return True
            
        except Exception as e:
            logger.error(f"❌ Error validando datos: {str(e)}")
            return False
    
    def ejecutar_extraccion(self) -> List[Dict[str, Any]]:
        """
        Ejecuta la extracción completa para todas las ciudades
        
        Returns:
            Lista de diccionarios con datos de cada ciudad
        """
        datos_extraidos = []
        ciudades_exitosas = 0
        ciudades_fallidas = 0
        
        logger.info(f"🔄 Iniciando extracción para {len(self.ciudades)} ciudades...")
        
        for ciudad in self.ciudades:
            try:
                # Extrae datos
                response = self.extraer_clima(ciudad)
                if not response:
                    ciudades_fallidas += 1
                    continue
                
                # Procesa datos
                datos_procesados = self.procesar_respuesta(response)
                if not datos_procesados:
                    ciudades_fallidas += 1
                    continue
                
                # Valida datos
                if not self.validar_datos(datos_procesados):
                    logger.warning(f"⚠️  Datos de {ciudad} no pasaron validación")
                    ciudades_fallidas += 1
                    continue
                
                # Agrega a resultado
                datos_extraidos.append(datos_procesados)
                ciudades_exitosas += 1
                
            except Exception as e:
                logger.error(f"❌ Error procesando {ciudad}: {str(e)}")
                ciudades_fallidas += 1
        
        # Log de resumen
        logger.info("=" * 70)
        logger.info("RESUMEN DE EXTRACCIÓN")
        logger.info("=" * 70)
        logger.info(f"✅ Exitosas: {ciudades_exitosas}/{len(self.ciudades)}")
        logger.info(f"❌ Fallidas: {ciudades_fallidas}/{len(self.ciudades)}")
        logger.info(f"📊 Registros guardados: {len(datos_extraidos)}")
        
        return datos_extraidos
    
    def guardar_csv(self, datos: List[Dict[str, Any]], archivo: str = 'data/clima.csv') -> bool:
        """
        Guarda datos en formato CSV
        
        Args:
            datos: Lista de diccionarios con datos
            archivo: Ruta del archivo a guardar
            
        Returns:
            True si se guardó correctamente
        """
        try:
            # Crear directorio si no existe
            os.makedirs(os.path.dirname(archivo), exist_ok=True)
            
            # Convertir a DataFrame
            df = pd.DataFrame(datos)
            
            # Guardar CSV
            df.to_csv(archivo, index=False, encoding='utf-8')
            logger.info(f"💾 CSV guardado: {archivo}")
            logger.info(f"   - Filas: {len(df)}")
            logger.info(f"   - Columnas: {len(df.columns)}")
            
            return True
            
        except Exception as e:
            logger.error(f"❌ Error guardando CSV: {str(e)}")
            return False
    
    def guardar_json(self, datos: List[Dict[str, Any]], archivo: str = 'data/clima.json') -> bool:
        """
        Guarda datos en formato JSON
        
        Args:
            datos: Lista de diccionarios con datos
            archivo: Ruta del archivo a guardar
            
        Returns:
            True si se guardó correctamente
        """
        try:
            # Crear directorio si no existe
            os.makedirs(os.path.dirname(archivo), exist_ok=True)
            
            # Guardar JSON
            with open(archivo, 'w', encoding='utf-8') as f:
                json.dump(datos, f, indent=2, ensure_ascii=False)
            
            logger.info(f"💾 JSON guardado: {archivo}")
            logger.info(f"   - Registros: {len(datos)}")
            
            return True
            
        except Exception as e:
            logger.error(f"❌ Error guardando JSON: {str(e)}")
            return False
    
    def mostrar_tabla(self, datos: List[Dict[str, Any]]):
        """
        Muestra los datos en formato de tabla
        
        Args:
            datos: Lista de diccionarios con datos
        """
        try:
            df = pd.DataFrame(datos)
            
            # Seleccionar columnas para mostrar
            columnas_mostrar = ['ciudad', 'temperatura_c', 'humedad', 'velocidad_viento_kmh', 'descripcion']
            df_mostrar = df[columnas_mostrar].copy()
            
            # Renombrar para mejor legibilidad
            df_mostrar.columns = ['Ciudad', 'Temp (°C)', 'Humedad (%)', 'Viento (km/h)', 'Descripción']
            
            print("\n" + "="*80)
            print("DATOS EXTRAÍDOS - TABLA RESUMEN")
            print("="*80)
            print(df_mostrar.to_string(index=False))
            print("="*80 + "\n")
            
        except Exception as e:
            logger.error(f"❌ Error mostrando tabla: {str(e)}")


# ============================================================================
# FUNCIÓN PRINCIPAL
# ============================================================================

def main():
    """Función principal de ejecución"""
    try:
        # Crear extractor
        extractor = WeatherstackExtractor()
        
        # Ejecutar extracción
        datos = extractor.ejecutar_extraccion()
        
        if not datos:
            logger.error("❌ No se obtuvieron datos. Verifica:")
            logger.error("   1. Tu API_KEY en .env es correcta")
            logger.error("   2. Tienes conexión a internet")
            logger.error("   3. El plan free permite más solicitudes")
            return False
        
        # Guardar en múltiples formatos
        extractor.guardar_csv(datos)
        extractor.guardar_json(datos, 'data/clima.json')
        
        # Mostrar tabla
        extractor.mostrar_tabla(datos)
        
        # Generar diagramas (opcional)
        try:
            from etl_diagram import DiagramaETL
            logger.info("🎨 Generando diagramas del pipeline...")
            diagrama = DiagramaETL()
            diagrama.generar_todos_diagramas()
        except ImportError:
            logger.warning("⚠️  etl_diagram.py no encontrado, saltando diagramas")
        
        logger.info("\n✅ PIPELINE ETL COMPLETADO EXITOSAMENTE")
        return True
        
    except ValueError as e:
        logger.error(f"❌ Error de configuración: {str(e)}")
        return False
    except Exception as e:
        logger.error(f"❌ Error inesperado: {str(e)}")
        return False


if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
