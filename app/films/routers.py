"""Modulo Films Routers

También se conoce como recursos.
Toda API REST se basa en acceder y/o manipular recursos.
Para ello, las APIs utilizan el protocolo HTTP y alguno de sus verbos.
Generalmente, los verbos más utilizados en un API REST son los siguientes::

    GET: Para obtener un recurso o colección.
    POST: Para crear un recurso (y/o añadirlo a una colección).
    PUT/PATCH: Para modificar un recurso.
    DELETE: Para eliminar un recurso.

Para implementar los recursos en Flask haremos uso de la extensión Flask-Restful. Otra forma puede
ser usar Flask puro definiendo rutas para los endpoints. Tener en cuenta:
Flask-Restful si el proyecto tiene fechas de entrega cortas y se necesita tener un MVP
corriendo pronto.
Si el proyecto es pequeño en alcance y tamaño entonces Flask puro podría servir.

En Flask-Restful un recurso no es más que una clase asociada a un endpoint (la URL mediante la que
se expone el recurso) que define cómo se puede acceder y/o manipular dicho recurso.
Para ello, solo hay que implementar los métodos correspondientes a cada uno de los verbos HTTP que
se necesiten.

Veámoslo en acción. En nuestro caso vamos a crear dos recursos diferentes:

    - Colección de películas: Este recurso es en realidad una colección que permitirá obtener el
      catálogo completo de películas y añadir una nueva al catálogo.
    - Película: Este recurso obtendrá una película del catálogo a partir de su id.

**Pasos a seguir**:
    - Definir un Blueprint llamado films_bp. Siguiendo esta filosofía, podremos crear nuevos
      recursos en otros paquetes de la aplicación.
    - Crear una instancia del Api a partir del blueprint anterior. Esta variable api es muy similar
      a un blueprint, solo que expone métodos propios de un Api de Flask-Restful.
    - Crear una instancia del esquema FilmSchema.
    - Definir el recurso FilmListResource asociado a la URL /api/films/.
      Todo recurso en Flask-Restful debe heredar de la clase Resource.
    - Definir el recurso FilmResource asociado a la URL /api/films/<film_id>.
      film_id será un parámetro que se defina en cada uno de los métodos del recurso.
"""
from flask import request, Blueprint
from flask_restful import Api, Resource

from .schemas import FilmSchema
from .models import Film, Actor
from ..error_handling import ObjectNotFound


films_bp = Blueprint('films_bp', __name__)
film_schema = FilmSchema()
api = Api(films_bp)


class FilmListResource(Resource):
    def get(self):
        """Método GET

        Como se puede apreciar, lo que hace este método es obtener en films
        el listado de objetos del modelo Film, serializarlos y devolver el JSON
        resultante. La serialización se realiza llamando al método dump() del
        esquema correspondiente. A este método se le pasa el objeto a
        serializar. En caso de que sea un listado, como ocurre aquí,
        hay que indicar el argumento many=True.
        """
        films = Film.get_all()
        result = film_schema.dump(films, many=True)
        return result

    def post(self):
        """Método POST

        En primer lugar obtiene el cuerpo de la respuesta en formato JSON.
        Para ello, se llama al método get_json() del objeto request.
        A continuación se llama al método load() del esquema film_schema.
        Este método valida que el JSON data cumpla con el esquema.
        A su vez, se crea el diccionario film_dict a partir del JSON original.
        Se crea una instancia de Film a partir de los datos del diccionario y
        se guarda.
        Se serializa el objeto film y se devuelve en la respuesta.
        Fíjate que en esta ocasión también se indica el código de respuesta.
        En este caso 201, que significa que se creó un objeto.
        """
        data = request.get_json()
        film_dict = film_schema.load(data)
        film = Film(title=film_dict['title'],
                    length=film_dict['length'],
                    year=film_dict['year'],
                    director=film_dict['director']
                    )
        for actor in film_dict['actors']:
            film.actors.append(Actor(actor['name']))
        film.save()
        resp = film_schema.dump(film)
        return resp, 201


class FilmResource(Resource):
    def get(self, film_id):
        """Método GET

        Obtiene información de película a partir de su id.
        """
        film = Film.get_by_id(film_id)
        if film is None:
            raise ObjectNotFound('La película no existe')
        resp = film_schema.dump(film)
        return resp


# Se agregan los recursos
api.add_resource(FilmListResource, '/api/films/',
                 endpoint='film_list_resource')
api.add_resource(FilmResource, '/api/films/<int:film_id>',
                 endpoint='film_resource')
