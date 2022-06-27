"""Módulo de aplicación.

En este módulo se implementa el método factoría que crea la app de Flask.
Además se registran los manejadores de errores para los códigos de respuesta y excepciones no
controladas. Fíjate cómo aquí se maneja la excepción ObjectNotFound, devolviendo un mensaje
JSON con el error y el código de respuesta 404.

"""
from flask import Flask, jsonify
from flask_restful import Api

from app.error_handling import ObjectNotFound, AppErrorBaseClass
from app.database import db
from app.films.routers import films_bp
from .ext import ma, migrate


def create_app(settings_module):
    """Crear aplicación

    Contiene las funciones necesarias para crear la aplicación.
    Recibe como parámetro una configuración de entorno.
    """
    app = Flask(__name__)
    app.config.from_object(settings_module)

    # Inicializa las extensiones
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    # Captura todos los errores 404
    Api(app, catch_all_404s=True)

    # Deshabilita el modo estricto de acabado de una URL con /
    app.url_map.strict_slashes = False

    # Registra los blueprints
    app.register_blueprint(films_bp)

    # Registra manejadores de errores personalizados
    register_error_handlers(app)
    return app


def register_error_handlers(app):
    """Registro de errores.

    Interpreta las excepciones y los registra a nivel de aplicación.
    """
    @app.errorhandler(Exception)
    def handle_exception_error(e):
        return jsonify({'msg': 'Internal server error'}), 500

    @app.errorhandler(405)
    def handle_405_error(e):
        return jsonify({'msg': 'Method not allowed'}), 405

    @app.errorhandler(403)
    def handle_403_error(e):
        return jsonify({'msg': 'Forbidden error'}), 403

    @app.errorhandler(404)
    def handle_404_error(e):
        return jsonify({'msg': 'Not Found error'}), 404

    @app.errorhandler(AppErrorBaseClass)
    def handle_app_base_error(e):
        return jsonify({'msg': str(e)}), 500

    @app.errorhandler(ObjectNotFound)
    def handle_object_not_found_error(e):
        return jsonify({'msg': str(e)}), 404
