"""Módulo de ejecución

Básicamente, en este módulo se crea la instancia de la app de Flask indicando dónde están definidos
los parámetros de configuración (el fichero de configuración se especifica en la variable de
entorno APP_SETTINGS_MODULE).
Las variables de entorno se definen en el archivo .flaskenv con el fin de poder ejecutar los
comandos flask (flask run, flask db)
"""
import os

from app import create_app

settings_module = os.getenv('APP_SETTINGS_MODULE')
app = create_app(settings_module)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
