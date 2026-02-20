# Define proyectos without emojis in the array (add them in HTML)
$proyectos = @(
    @{num=3; titulo="Exploración de Datos Espaciales"; api="SpaceX API"; emoji="[rocket]"; url="https://docs.spacexdata.com/"; desc="Ingiere y analiza datos públicos de SpaceX incluyendo lanzamientos, cohetes y destinos."; sugerencias=$("Analizar patrones de lanzamientos", "Predecir próximas misiones", "Visualizar trayectorias de cohetes", "Comparar tasas de éxito")}
    @{num=4; titulo="Datos Astronómicos de NASA"; api="NASA API"; emoji="[galaxy]"; url="https://api.nasa.gov/"; desc="Accede a múltiples APIs de NASA para recopilar datos sobre asteroides, imágenes y fenómenos astronómicos."; sugerencias=$("Detectar asteroides cercanos", "Analizar imágenes espaciales", "Predecir trayectorias de asteroides", "Historias de descubrimientos")}
    @{num=5; titulo="Base de Datos de Superhéroes"; api="Superhero API"; emoji="[superhero]"; url="https://superheroapi.com/"; desc="Accede a una base de datos completa de superhéroes con información de poderes, afiliaciones y biografías."; sugerencias=$("Analizar distribución de poderes", "Clasificar superhéroes por fortaleza", "Predecir poder faltante", "Agrupar por afiliación")}
    @{num=6; titulo="Base de Datos de Películas"; api="OMDb API"; emoji="[movie]"; url="https://www.omdbapi.com/"; desc="Construye un ETL que recopile información de películas incluyendo calificaciones, géneros y actores."; sugerencias=$("Sistema de recomendación", "Análisis de géneros populares", "Predicción de calificaciones", "Análisis de actores frecuentes")}
    @{num=7; titulo="Catálogo de Videojuegos"; api="IGDB API"; emoji="[games]"; url="https://www.igdb.com/api"; desc="Desarrolla un ETL que acceda a la base de datos de videojuegos con análisis de tendencias."; sugerencias=$("Análisis de plataformas", "Predicción de calificaciones", "Tendencias de géneros", "Análisis de desarrolladores")}
    @{num=8; titulo="Indicadores Económicos de Colombia"; api="World Bank API"; emoji="[world]"; url="https://data.worldbank.org/developers"; desc="Obtén indicadores económicos y demográficos de Colombia y compara con otros países."; sugerencias=$("Comparativa regional", "Análisis histórico de indicadores", "Predicción de PIB", "Clustering de países similares")}
    @{num=9; titulo="Atlas de Países y Territorios"; api="REST Countries API"; emoji="[globe]"; url="https://restcountries.com/"; desc="Obtén información completa sobre todos los países del mundo incluyendo población y datos geográficos."; sugerencias=$("Mapas interactivos", "Comparativas demográficas", "Análisis por región", "Clustering de países")}
    @{num=10; titulo="Catálogo de Anime y Manga"; api="Jikan API"; emoji="[anime]"; url="https://jikan.moe/"; desc="Accede a la base de datos más grande de anime y manga a través de Jikan."; sugerencias=$("Análisis de géneros", "Predicción de puntuaciones", "Estadísticas por temporada", "Recomendador de anime")}
    @{num=11; titulo="Base de Datos Pokémon"; api="PokéAPI"; emoji="[lightning]"; url="https://pokeapi.co/"; desc="Utiliza PokéAPI para crear una base de datos completa de Pokémon con estadísticas y evoluciones."; sugerencias=$("Análisis de balanceo", "Predicción de efectividad", "Generador de equipos", "Análisis de tipos")}
    @{num=12; titulo="Base de Datos de Los Simpsons"; api="The Simpsons API"; emoji="[tv]"; url="https://thesimpsonsapi.com/"; desc="Accede a la base de datos completa del universo de Los Simpsons con 1182+ personajes y 768+ episodios."; sugerencias=$("Análisis de frases icónicas", "Clustering de personajes", "Evolución de personajes", "Análisis de temporadas")}
    @{num=13; titulo="Análisis de Tasas de Cambio"; api="Exchange Rate API"; emoji="[exchange]"; url="https://exchangerate-api.com/"; desc="Monitorea tasas de cambio de múltiples monedas en tiempo real y predice fluctuaciones."; sugerencias=$("Predicción de tasas", "Análisis de volatilidad", "Tendencias históricas", "Alertas de cambio")}
    @{num=14; titulo="Blog de Usuarios Sintéticos"; api="JSONPlaceholder API"; emoji="[note]"; url="https://jsonplaceholder.typicode.com/"; desc="Utiliza JSONPlaceholder para crear un ETL con posts, comentarios y datos de usuarios."; sugerencias=$("Sistema de recomendación", "Análisis de engagement", "Detección de comunidades", "Análisis de red social")}
    @{num=15; titulo="Análisis de Suscriptores YouTube"; api="YouTube Data API"; emoji="[video]"; url="https://developers.google.com/youtube/v3"; desc="Analiza canales de YouTube populares y predice tendencias de contenido."; sugerencias=$("Predicción de views", "Análisis de sentimiento", "Recomendador de videos", "Tendencias de contenido")}
)

# Función para convertir emojis simbólicos a reales
function ConvertEmoji([string]$emoji) {
    switch($emoji) {
        "[rocket]" { return "🚀" }
        "[galaxy]" { return "🌌" }
        "[superhero]" { return "🦸" }
        "[movie]" { return "🎬" }
        "[games]" { return "🎮" }
        "[world]" { return "🌍" }
        "[globe]" { return "🌐" }
        "[anime]" { return "🎌" }
        "[lightning]" { return "⚡" }
        "[tv]" { return "📺" }
        "[exchange]" { return "💱" }
        "[note]" { return "📝" }
        "[video]" { return "▶️" }
        default { return $emoji }
    }
}

$baseDir = "c:\Users\DELL\Documents\GitHub\material-mineria-datos\BaseProjects\scorm-proyectos"

foreach($proyecto in $proyectos) {
    $num = $proyecto.num.ToString().PadLeft(2, '0')
    $titulo = $proyecto.titulo
    $api = $proyecto.api
    $emoji = ConvertEmoji $proyecto.emoji
    $url = $proyecto.url
    $desc = $proyecto.desc
    
    $sugerenciasHtml = ""
    foreach($sug in $proyecto.sugerencias) {
        $sugerenciasHtml += "<li>$sug</li>"
    }

    $html = @"
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Proyecto $($proyecto.num): $titulo</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="css/styles.css">
</head>
<body>
    <header class="main-header">
        <div class="top-bar">
            <div class="container">
                <div class="brand-container">
                    <div>
                        <div class="brand-name">INGENIERÍA DE SISTEMAS</div>
                        <div style="font-size: 0.9em; margin-top: 5px;">Minería de Datos</div>
                    </div>
                </div>
            </div>
        </div>
    </header>

    <main class="main-content">
        <div class="container">
            <div class="project-card active">
                <div class="project-title">
                    <div class="project-number">$($proyecto.num)</div>
                    <div>
                        <h3>$titulo</h3>
                        <span class="api-tag">$emoji $api</span>
                    </div>
                </div>

                <div class="project-content">
                    <p class="description">$desc</p>

                    <div class="api-link">
                        <strong>API:</strong> <a href="$url" target="_blank">$url</a>
                    </div>

                    <div class="deliverables">
                        <h5><i class="fas fa-clipboard-list"></i> Entregables</h5>
                        <ol>
                            <li><strong>Extractor ETL:</strong> Script que extrae datos de la API con manejo de errores</li>
                            <li><strong>BD PostgreSQL:</strong> Diseño de tablas optimizado para los datos de la API</li>
                            <li><strong>Dashboard Streamlit:</strong> Visualizaciones interactivas y análisis exploratorio</li>
                            <li><strong>Docker Compose:</strong> Contenedores orquestados con servicios integrados</li>
                            <li><strong>ML Jupyter:</strong> Modelos de machine learning y análisis predictivo</li>
                            <li><strong>Presentación PPT:</strong> Problema identificado, alcance del proyecto, pregunta de investigación, herramientas usadas, arquitectura de datos, modelos implementados, métricas de evaluación, resultados obtenidos y recomendaciones</li>
                        </ol>
                    </div>

                    <div class="reflection-box">
                        <h4>💡 Sugerencias de Análisis</h4>
                        <ul style="margin-left: 20px;">
                            $sugerenciasHtml
                        </ul>
                    </div>
                </div>
            </div>

            <hr class="divider-thick">

            <section style="text-align: center; margin-top: 40px;">
                <a href="proyecto-$(($proyecto.num-1).ToString().PadLeft(2, '0')).html" style="display: inline-block; padding: 10px 20px; background: #2a5298; color: white; text-decoration: none; border-radius: 5px; margin-right: 10px;">← Anterior</a>
                <a href="intro.html" style="display: inline-block; padding: 10px 20px; background: #2a5298; color: white; text-decoration: none; border-radius: 5px; margin-right: 10px;">Introducción</a>`
+ (if($proyecto.num -lt 15) { "<a href=`"proyecto-$(($proyecto.num+1).ToString().PadLeft(2, '0')).html`" style=`"display: inline-block; padding: 10px 20px; background: #ff6b6b; color: white; text-decoration: none; border-radius: 5px;`">Siguiente →</a>" } else { "" })
+ @"
            </section>
        </div>
    </main>

    <footer style="text-align: center; padding: 30px 20px; background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%); color: white; margin-top: 60px;">
        <p style="margin: 0; font-size: 14px;">© 2025 Ingeniería de Sistemas - Minería de Datos. Todos los derechos reservados.</p>
        <p style="margin-top: 15px; font-size: 16px; font-weight: 500;">Creado por <strong>Ing. Julian Andres Quimbayo Castro</strong></p>
    </footer>

    <script src="js/scripts.js"></script>
</body>
</html>
"@

    $filePath = "$baseDir\proyecto-$num.html"
    Set-Content -Path $filePath -Value $html -Encoding UTF8
    Write-Host "✓ Creado: proyecto-$num.html"
}

Write-Host "✓ Todos los proyectos han sido creados exitosamente"
