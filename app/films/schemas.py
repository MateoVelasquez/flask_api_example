"""Modulo Films Schemas

Para definir los esquemas utilizaremos Flask-Marshmallow.
Un esquema es una clase que define cómo se serializa un modelo/recurso consumido por el API a JSON.

Los esquemas se definen de manera muy similar a los modelos, solo que, para los campos,
hay que utilizar los tipos definidos por Marshmallow.

Además, para que la serialización se realice de forma automática, los nombres de cada uno de los
campos del esquema deben ser idénticos a los nombres de los atributos del modelo que representan.
Cuando Marshmallow encuentre un campo en el esquema que coincida con el nombre de un atributo
en el modelo, tratará de serializarlo. Fíjate también de que los campos sean de un tipo compatible.


Observa que al campo id se le pasa como argumento dump_only=True.
Esto hará que solo se tenga en cuenta este campo a la hora de serializar el objeto
(y no en la carga).
Por otro lado, observa que el campo actors en el esquema FilmSchema se define como Nested.
Esto indica que el esquema FilmSchema contiene varios (many=True) elementos de tipo ActorSchema.
"""
from marshmallow import fields

from app.ext import ma


class FilmSchema(ma.Schema):
    """Esquema de películas
    """
    id = fields.Integer(dump_only=True)
    title = fields.String()
    length = fields.Integer()
    year = fields.Integer()
    director = fields.String()
    actors = fields.Nested('ActorSchema', many=True)


class ActorSchema(ma.Schema):
    """Esquema de actores
    """
    id = fields.Integer(dump_only=True)
    name = fields.String()
