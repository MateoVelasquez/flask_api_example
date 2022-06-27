# Flask API Ejemplo
Ejemplo de API usando FLASK. Esta sencilla aplicación web se desarrolla con el fin de ampliar el conocimiento sobre la estructura de un desarrollo web mediante herramientas como los son Python y Flask (junto con sus derivados).

La API consiste en un catálogo de películas que permite consultarse de forma completa o individual, y adicionalmente se puede conocer la lista de actores participantes registrados para cada film.

Este proyecto se desarrolla siguiendo el tutorial construido por el Ingeniero Informático Juan José Lozano Gómez, el cual se puede encontrar [aquí](https://j2logo.com/flask/tutorial-como-crear-api-rest-python-con-flask/).

Adicionalmente, se implementa la documentación automática usando Sphinx acorde a lo explicado en este [tutorial](https://www.cosmoscalibur.com/blog/crear-documentacion-de-un-proyecto-python-con-sphinx/)

## Comenzando 🚀

Se requiere tener previamente instalado Anaconda. La estructura de proyecto utilizada es la siguiente:
```
+flask_api_example
    |_+ app
        |_+films
            | __init__.py
            | models.py
            | routers.py
            | schemas.py
        | __init__.py
        | database.py
        | error_handling.py
        | ext.py
    |_+ configuration
        | __init__.py
        | default.py
    |_+ docs
    |_+ test
        | testservice.py
    | .flaskenv
    | run.py
    | environment.yml
    | README.md
```


### Instalación ambiente de desarrollo 📋

Esta aplicación se desarrolla en Flask. El archivo *environment.yml* cuenta con las dependencias mínimas necesarias para que el aplicativo funcione. Para instalarlas, se debe ejecutar la siguiente instrucción en una consola de anaconda o miniconda luego de haber clonado el repositorio.

```
> conda env create -f environment.yml
> conda activate flaskdev
```
A continuación es necesario crear la base de datos, esto se logra mediante los comandos:

```
> flask db init
> flask db migrate -m "Initalize db"
> flask db upgrade
```

Finalmente, se puede ejecutar el aplicativo usando el comando:

```
flask run
```

## Ejecutando las pruebas ⚙️

En el presente repositorio, dentro de la carpeta test, se incluye un archivo de pruebas *testservice.py* que contiene dos funciones principales para probar el método POST y el método GET.

Ubicando la consola en el directorio test, ejecutar el siguiente comando para ingresar un objeto a la base de datos (método POST):

```
python -c "import testservice; testservice.test_post()"
```

Finalmente podemos consultar el objeto agregado mediante el comando (método GET):

```
python -c "import testservice; testservice.test_get()"
```

## Despliegue 📦

Se puede ejecutar el aplicativo usando el comando:

```
flask run
```

Algunos endpoints de interés:

- /api/films : Devuelve lista de películas registradas
- /api/films/(id) : Devuelve la película asociada al id proporcionado

## Construido con 🛠️

Este aplicativo se realizó usando el Framework Flask para Python

* [flask](https://flask.palletsprojects.com/en/2.1.x/) - El framework web usado.



## Tutorial original 📖

Puedes encontrar mucho más sobre este proyecto proyecto en el tutorial original [Tutorial](https://j2logo.com/flask/tutorial-como-crear-api-rest-python-con-flask/)

## Versionado 📌

Este proyecto utiliza un esquema de versionado semántico. Para todas las versiones disponibles, mira los [tags en este repositorio](https://github.com/MateoVelasquez/flask_api_example/tags).
