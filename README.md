# DuDe (Duplicate Detector)

## Como funciona?
DuDe, abreviatura de _"Duplicate Detector"_ (Detector de Duplicados), es un programa que utiliza dos técnicas principales para identificar imágenes duplicadas: OCR (Reconocimiento Óptico de Caracteres) y tablas de hash.

* **OCR (Reconocimiento Óptico de Caracteres):** Esta técnica se encarga de extraer texto de imágenes. El programa utiliza la biblioteca `pytesseract` para realizar OCR en cada imagen del conjunto de datos.

* **Tablas de Hash:** Una tabla de hash es una estructura de datos que asocia claves con valores. En este caso, se utiliza para almacenar el texto extraído de las imágenes junto con los primeros caracteres de ese texto. Esto permite una rápida comparación y búsqueda de duplicados.

El proceso de detección de duplicados funciona de la siguiente manera:

1. El programa comienza inicializando un objeto DuDe con el directorio que contiene las imágenes que se desean analizar.

1. Luego, para cada imagen en el directorio, se realiza el siguiente proceso:

   1. Se realiza OCR en la imagen para extraer el texto contenido en ella.

   2. Se toman los primeros caracteres del texto obtenido como una identificación única de la imagen (en este caso, los dos primeros caracteres).

   3. Se compara esta identificación con las identificaciones previamente registradas en la tabla de hash.

   4. Si se encuentra una coincidencia, se compara el texto completo de la imagen con otras imágenes que tengan la misma identificación inicial. Si se detecta una similitud significativa entre los textos de las imágenes, se registran como duplicadas.

   5. Si no se encuentra una coincidencia, se registra la identificación junto con el nombre del archivo en la tabla de hash.

1. Una vez que se han analizado todas las imágenes, el programa proporciona dos funciones para obtener los resultados:

   1. **get_duplicates():** Devuelve un JSON que contiene los nombres de los archivos duplicados y el archivo del que son duplicados.

   2. **get_hash_map():** Devuelve un JSON que representa la tabla de hash utilizada para identificar duplicados.