"""Modulo database

Instanciación para SQLAlchemy y adicionalmente creamos la clase BaseModelMixin,
la cual es de utilidad para el manejo de los modelos.


Flask SQLAlchemy: Librería para interactuar con la base de datos a través de su ORM.
más información aquí:
`https://j2logo.com/tutorial-flask-leccion-5-base-de-datos-con-flask-sqlalchemy/`
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class BaseModelMixin:

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get(id)

    @classmethod
    def simple_filter(cls, **kwargs):
        return cls.query.filter_by(**kwargs).all()
