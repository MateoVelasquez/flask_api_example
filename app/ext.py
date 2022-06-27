"""Modulo extensiones.

En este modulo se realiza la instanciación de las extensiones usadas
en la aplicación.
En este caso, Flask-Marshmallow y Flask-Migrate. El hacerlo en este fichero
evita que se produzcan referencias circulares cuando se utilicen a lo largo
de la aplicación.

- **Flask Marshmallow**: Es una extensión que facilita la serialización de los modelos de la base de
  datos a JSON y viceversa. Está basada en Marshmallow.
- **Flask Migrate**: Esta extensión permite generar las tablas de la base de datos a partir de
  ficheros de migración. Puedes encontrar más información aquí.
"""
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

ma = Marshmallow()
migrate = Migrate()
