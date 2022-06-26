"""Configuración por defecto.

Mas información: ´https://j2logo.com/tutorial-flask-leccion-7-parametros-de-configuracion-proyecto/´


Los parámetros de configuración son:
    SECRET_KEY: Lo utilizan Flask y ciertas extensiones que manejan aspectos de seguridad.
    PROPAGATE_EXCEPTIONS: Para propagar las excepciones y poder manejarlas a nivel de aplicación.
    SQLALCHEMY_DATABASE_URI: URI de la base de datos.
    SQLALCHEMY_TRACK_MODIFICATIONS: Se desactiva como indica la documentación.
    SHOW_SQLALCHEMY_LOG_MESSAGES = Se deshabilitan los mensajes de log de SQLAlchemy.
    ERROR_404_HELP: Deshabilita las sugerencias de otros endpoints relacionados con alguno que no
    exista (Flask-Restful).
"""

SECRET_KEY = '123447a47f563e90fe2db0f56b1b17be62378e31b7cfd3adc776c59ca4c75e2fc512c15f69bb38307d11d5d17a41a7936789' #noqa
PROPAGATE_EXCEPTIONS = True

# Configuración FLask
ERROR_404_HELP = False

# Configuración de conexión a base de datos.
SQLALCHEMY_DATABASE_URI = 'sqlite:///films.sqlite'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SHOW_SQLALCHEMY_LOG_MESSAGES = False
