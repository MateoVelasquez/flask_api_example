Ambiente de desarrollo
======================

Código fuente y estructura de proyecto
--------------------------------------

El código fuente del proyecto se encuentra en el repositorio:
`https://github.com/MateoVelasquez/flask_api_example` se puede clonar mediante GIT.

La estructura de proyecto es la siguiente::

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

Este aplicativo se realizó usando el Framework Flask para Python: `https://flask.palletsprojects.com/en/2.1.x/`

Dependencias
------------
Se requiere tener previamente instalado el gestor de paquetes Anaconda (o en su defecto miniconda).
Esta aplicación se desarrolla en Flask, el archivo *environment.yml* cuenta con
las dependencias mínimas necesarias para que el aplicativo funcione.
Para instalarlas, se debe ejecutar la siguiente instrucción en una consola de
anaconda o miniconda luego de haber clonado el repositorio::

    > conda env create -f environment.yml
    > conda activate flaskdev

A continuación es necesario crear la base de datos, esto se logra mediante los comandos::

    > flask db init
    > flask db migrate -m "Initalize db"
    > flask db upgrade

Finalmente, se puede ejecutar el aplicativo usando el comando::

    flask run


Despliegue y uso
================

Se puede ejecutar el aplicativo usando el comando::

    flask run

Algunos endpoints de interés:

- /api/films : Devuelve lista de películas registradas
- /api/films/(id) : Devuelve la película asociada al id proporcionado