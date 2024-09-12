# 🎵 Popatoms

Este proyecto tiene como objetivo analizar los grandes éxitos musicales de los últimos 50 años para comprender la influencia de distintos factores en la popularidad de las canciones así como la evolución de estas. Utilizando datos extraídos de la API de Spotify y la API de Billboard, exploramos características como la energía, el tempo, la duración y otros atributos para entender su relación con el éxito en las listas musicales.

## 📁 Estructura del Proyecto

El proyecto está organizado en los siguientes archivos y carpetas clave:

- `main.py`: El archivo principal del proyecto que ejecuta el análisis general, la recopilación de datos, el preprocesamiento y el análisis.
- `functions.py`: Contiene funciones auxiliares para interactuar con las APIs, realizar el procesamiento de datos y manipular los resultados.
- `eda.ipynb`: Un notebook que realiza el Análisis Exploratorio de Datos (EDA) y visualiza los resultados en gráficos. Aquí es donde exploramos los datos en profundidad.
- `requirements.txt`: Lista de las dependencias necesarias para ejecutar el proyecto.
- `README.md`: Este archivo, que describe el propósito del proyecto y cómo ejecutarlo.

## 🔧 Instalación y Configuración

Clona este repositorio:

```bash
git clone https://github.com/tu-usuario/tu-proyecto.git
cd tu-proyecto
```

Instala las dependencias necesarias:
```bash
pip install -r requirements.txt
```
Configura las claves de las APIs de Spotify y Billboard. Debes crear un archivo .env en la raíz del proyecto y agregar tus credenciales:

```bash
SPOTIFY_CLIENT_ID=tu_client_id
SPOTIFY_CLIENT_SECRET=tu_client_secret
BILLBOARD_API_KEY=tu_billboard_api_key
```
# 🚀 Ejecución del Proyecto

**Ejecutar el archivo principal:** Para comenzar con el análisis y la extracción de datos, ejecuta el archivo `main.py`:

```bash
python main.py
```
