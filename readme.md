# Proyecto individual 1 - MLOps - Sistema de recomendación de peliculas

DATA SCIENCE - Machine Learning Operations (MLOps)

Este es el primer proyecto de los laboratorios del curso de Data Science de Soy Henry. En el se debe seguir una serie de pasos con el objetivo de desarrollar un proceso de Data Engineering sobre unos datasets que contienen información sobre películas, simulando un entorno real de trabajo con el que se tiene que lograr un MVP (mínimo producto viable). Dicho MVP debe cumplir con ciertas consignas, entre ellas un modelo de Machine Learning de recomendación de películas, y luego ser deployado a través de una API que pueda ser consumida en la plataforma RENDER

# Fuentes de datos para realizar el MVP:
los datos usados para realizar el MVP se encuentran en dos archivos formato csv alojados en la siguiente dirección de google drive: https://drive.google.com/drive/folders/1X_LdCoGTHJDbD28_dJTxaD4fVuQC9Wt5

# De este repositorio
- "_pycache_" y "entorno_movies" son carpetas de archivos del entorno creado localmente.
- ".gitattributes" archivo de texto utilizado en Git para asignar atributos a archivos y directorios dentro de un repositorio.
- "Noteb_ETL_y_EDA_endpoints.ipynb" el notebook donde se realizo todo el ETL y el EDA, también se hicieron allí los endpoints.
- "dataset_final.csv" el archivo csv que se exporta luego del ETL para ser consumido por la API en los endpoints.
- "main.py" archivo de python donde esta la API.
- "requirements.txt" archivo de texto con los requerimientos para el deploy en render.

# Proceso de EDA y ETL

El proceso comienza totalmente desde cero, creando un entorno virtual de python donde se compaginaria todo el proyecto. Luego se crea un archivo de Jupiter Notebook donde se continuaría con todo el trabajo de ETL y EDA, asimismo con todas las pruebas y errores del desarrollo de la API.
Se continúo con la instalación de las librerias necesarias dentro del entorno virtual, para luego seguir con la importacion de los dataset fuente para realizar el MVP. Luego se realizó un EDA ligero para entender la estructura de los datos y analizar pequeñas modificaciones para ir efectuando mientras se practicaba el ETL obligatorio de acuerdo a a las expresas consignas del MVP. A saber, entre otras, se realizaron los siguiente cambios:
- Se eliminaron las columnas que no se necesitaban para el MVP, entre ellas, las indicadas en las consignas.
- Se aplanaron los datos que habia en columnas anidadas y se desecharon datos que no se necesitaban.
- Hemos aplicado cambios de formatos a algunas columnas para su manipulacion posterior, como convertir a datetime o convertir a float y, en algunos casos, convertir a cadenas de texto también.
- Tambíen hemos creado alguna columnas nuevas como "release_year" y #return".
- Se detectó nulos y duplicados durante el EDA, por lo tanto fueron subsanados, etc.
Todos estos cambios se pueden encontrar en el notebook de nombre "Noteb_ETL_y_EDA_endpoints.ipynb", así como el EDA a profundidad que se hizo para el modelo de machine learning.

# Endpoints del MVP

Luego de exportar a un nuevo archivo dataset_final.csv cuando se terminó el ETL, comenzamos a desarrollar los endpoints solicitados en el mismo archivo "Noteb_ETL_y_EDA_endpoints.ipynb", para luego transcribirlos al archivo "main.py" donde estaría todo el desarrollo de la API a traves del uso del framework FastAPI. Dicho desarrollo fue, seguidamente, deployado en la plataforma RENDER donde se puede corrobar a traves de este link: https://proyecto-movies-fm8m.onrender.com/docs que todas las funciones deployadas cumplen su consulta.

# Machine Learning

El último endpoint solicitado para en MVP fue el desarrollo de un sistema de recomendacin de películas. Para este se ha realizado un EDA a más profundiad a modo de poder tomar un criterio para seleccionar variables para el modelo. Dentro de los análisis efectuados se encuentran distribuciones de frecuencias de las variables numéricas, identificación de variables categóricas y sus valores, correlación entre variables, análisis temporales y por categoría. También nos hemos servido de algunos graficos de barras e histogramas, asi como matriz de relaciones de variables numéricas.
Se pueden visualizar las transformaciones y los análisis realizados en el archivo "Noteb_ETL_y_EDA_endpoints.ipynb"
Para el modelo de recomendación se decidío filtrar el dataset para las películas estrenadas a partir de 1987, ya que se detecto crecimiento exponencial aproximadamente a partir de dicho año. Luego de esta se trabajó con una muestra aleatoria de 10000 películas. Por último se hizo construyo un modelo basado en la similitud de coseno usando variables categóricas.

# Librerás utilizadas

Para realizar el MVP se utilizaron varias librerias de Python, algunas de estas las listamos a continuación:
- pandas: para la manipulación de datos y el ETL.
- numpy: para realizar operaciones matemáticas.
- fastAPI: para el desarrollo y prueba de la API.
- uvicorn: para el deploy de la API en la plataforma RENDER.
- scikit-learn: para el desarrollo del modelo de recomendación de películas.
- matplotlib y seaborn: para realizar los graficos de EDA
- RENDER: para el despliegue de la API en la web.
