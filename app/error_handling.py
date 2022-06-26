"""Módulo manejo de errores

En él se definen dos excepciones personalizadas.
Una general, AppErrorBaseClass, de la que heredarán todas la excepciones y errores de la aplicación
y ObjectNotFound, que utilizaremos cuando se intente acceder a un recurso que no existe.
"""


class AppErrorBaseClass(Exception):
    pass


class ObjectNotFound(AppErrorBaseClass):
    pass
