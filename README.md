mejorar el siguiente readme para un git:  

# Trabajo Final : Generador de letras de canciones a través de un modelo de neuronal recurrente
Este proyecto tiene como objetivo la generación automática de letras de canciones mediante el uso de un modelo de red neuronal recurrente (RNN). A continuación, se describe cómo se obtuvo y procesó el conjunto de datos de letras de canciones y los scripts utilizados en el proceso.

## Descripción del Proyecto
El generador de letras de canciones utiliza datos de la API de Genius (www.genius.com) para obtener las letras de canciones de una variedad de artistas. A partir de estos datos, se realizan los siguientes pasos:

· Obtención de Letras: Se utilizó la API de Genius para recolectar las letras de las canciones. El script lyricsgenius.py  interactúa con la API para obtener la información de las canciones y almacenar las letras correspondientes.

· Agrupación de Letras: Para consolidar todas las letras obtenidas en un único archivo, se utilizó el script get_lyrics_loop.py. Este script recorre los archivos .json generados por la API y agrupa las letras de las canciones en un solo archivo para su posterior procesamiento.

· Limpieza de Datos: Para eliminar palabras y puntuaciones no significativas (como "Verse", "Chorus", etc.), se empleó el script clean_csv.py. Este proceso asegura que las letras de las canciones estén limpias y listas para ser utilizadas por el modelo de red neuronal.

Todas el desarrollo se realizó en el entorno conda guardado DS.yml.
