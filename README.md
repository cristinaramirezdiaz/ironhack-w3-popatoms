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

Ejecutar el archivo principal: Para comenzar con el análisis y la extracción de datos, ejecuta el archivo main.py:

```bash
python main.py
```

Análisis Exploratorio de Datos (EDA): Si quieres visualizar gráficos y explorar los datos, abre el notebook eda.ipynb con Jupyter:

```bash
jupyter notebook eda.ipynb
```
# 📊 Descripción del Análisis

- API de Spotify: De esta API hemos obtenido datos relacionados con las características de las canciones, como el tempo, la energía, la duración, el modo, entre otros.
- API de Billboard: De esta API hemos extraído los rankings históricos de las canciones más populares, permitiendo hacer un análisis temporal.
El análisis se ha centrado en entender cómo estos atributos y características cambian a lo largo del tiempo y su impacto en la popularidad.

# 📈 Resultados y Conclusiones
Los resultados obtenidos a partir de los análisis gráficos y estadísticos revelan una serie de tendencias sobre cómo las características de las canciones exitosas han cambiado a lo largo de los últimos 50 años: 

 - 

# 💡 Hipótesis Iniciales
Antes de realizar el análisis, partimos de las siguientes hipótesis:

- Las canciones han reducido su duración en los últimos años (probablemente debido a la influencia de plataformas como TikTok).
- La música se ha vuelto más calmada, con un tempo más lento.
- Sin embargo, es probable que la intensidad del sonido (loudness) no haya disminuido.
- Las tonalidades menores se han vuelto más frecuentes en los últimos años.
- El compás más común sigue siendo el 4/4, con mucha diferencia.
- La música ha tendido a volverse más repetitiva en los últimos años.
- Los temas relacionados con la protesta, especialmente los que abordan el feminismo, son más comunes en la actualidad.
# 👥 Acerca del Equipo
Gabriela: https://www.linkedin.com/in/gabriela-casero-59233a131/
Almudena:  https://www.linkedin.com/in/almudenamcastro/
# 🛠️ Herramientas Utilizadas
- Lenguaje: Python
- APIs: Spotify, Billboard
- Librerías:
--  requests: Para la interacción con las APIs
--  pandas: Para la manipulación de datos
-- matplotlib / seaborn: Para la visualización de datos
- dotenv: Para gestionar las credenciales de las APIs
- jupyter: Para el análisis exploratorio
# 📝 Contribuciones
Si deseas contribuir a este proyecto, no dudes en enviar un pull request o reportar issues. Todos los comentarios y sugerencias son bienvenidos.

