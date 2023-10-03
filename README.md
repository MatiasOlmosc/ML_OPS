# ML_OPS

# Proyecto de Recomendación de Videojuegos en Steam

Bienvenido al proyecto de Recomendación de Videojuegos en Steam. Este proyecto tiene como objetivo crear un sistema de recomendación de videojuegos basado en el análisis de datos de la plataforma Steam. Como parte del equipo de Machine Learning Operations (MLOps), nuestro objetivo es llevar este sistema de recomendación desde el desarrollo del modelo hasta su implementación en producción.

## Descripción del Problema y Objetivos

### Contexto
Imagínate en el rol de un Data Scientist en Steam, una plataforma multinacional de videojuegos. Se te ha encomendado la tarea de crear un sistema de recomendación de videojuegos para usuarios. Si bien ya tenemos un modelo con buenas métricas, el desafío es llevarlo al mundo real y abordar desafíos significativos en los datos, como datos anidados y la falta de procesos automatizados para la actualización de productos.

### Objetivos
- Implementar un sistema de recomendación de videojuegos basado en el análisis de datos de usuarios y juegos en Steam.
- Desarrollar una API utilizando FastAPI para que los usuarios puedan acceder a las recomendaciones.
- Realizar análisis exploratorio de datos (EDA) para comprender mejor las relaciones y patrones en los datos.
- Entrenar un modelo de aprendizaje automático para crear un sistema de recomendación efectivo.
- Proporcionar recomendaciones de juegos basadas en similitud entre juegos.

## Estructura del Proyecto

### Transformaciones de Datos
En este MVP, no se requieren transformaciones de datos específicas, aunque se permiten si se justifican adecuadamente. También se permite eliminar columnas innecesarias para optimizar el rendimiento de la API y el entrenamiento del modelo.

### Análisis Exploratorio de los Datos (EDA)
Realizamos un análisis exploratorio de datos para comprender mejor las relaciones entre las variables del dataset, identificar outliers o anomalías y buscar patrones interesantes que puedan ser útiles en análisis posteriores. Evitamos el uso de librerías automáticas para EDA para poner en práctica los conceptos de forma manual.

### Desarrollo de la API
Utilizamos FastAPI para desarrollar una API que proporciona las siguientes consultas:
- `PlayTimeGenre(genero: str)`: Devuelve el año con más horas jugadas para un género dado.
- `UserForGenre(genero: str)`: Devuelve el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.
- `UsersRecommend(año: int)`: Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado.
- `UsersNotRecommend(año: int)`: Devuelve el top 3 de juegos MENOS recomendados por usuarios para el año dado.
- `sentiment_analysis(año: int)`: Según el año de lanzamiento, devuelve una lista con la cantidad de registros de reseñas de usuarios categorizados con un análisis de sentimiento.

### Deployment
Consideramos opciones de despliegue como Render, Railway u otros servicios que permiten que la API sea consumida desde la web. En nuestro caso, utilizamos Render por cuestiones de practicidad.

### Modelo de Aprendizaje Automático
Entrenamos un modelo de aprendizaje automático basado en similitud entre juegos para crear un sistema de recomendación item-item (juego-juego). Proporcionamos una función en la API para recibir recomendaciones basadas en este modelo.

### Video de Presentación
Creamos un video de no más de 7 minutos que muestra el funcionamiento de la API y explica brevemente el modelo utilizado para el sistema de recomendación.

## Criterios de Evaluación

- Prolijidad del código.
- Uso de clases y/o funciones, en caso de ser necesario.
- Código comentado y legible.
- Estructura organizada del repositorio.
- README.md que presente el proyecto y el trabajo realizado de manera comprensible.

## Fuente de Datos

- [Dataset](https://drive.google.com/drive/folders/1HqBG2-sUkz_R3h1dZU5F2uAzpRn7BSpj): Carpeta con el archivo que requiere ser procesado. Ten en cuenta que hay datos anidados en forma de diccionario o lista como valores en las filas.
- [Diccionario de datos](https://docs.google.com/spreadsheets/d/1-t9HLzLHIGXvliq56UE_gMaWBVTPfrlTf2D9uAtLGrk/edit#gid=0): Diccionario con algunas descripciones de las columnas disponibles en el dataset.

Este proyecto es un emocionante desafío que nos permite aplicar nuestros conocimientos en el mundo real y brindar a los usuarios recomendaciones de videojuegos personalizadas. ¡Esperamos que disfrutes explorando y utilizando este sistema de recomendación!
