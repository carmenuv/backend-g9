# sirve para autocompletar todos los parámetros en base a un modelo
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.usuarios import UsuarioModel

class UsuarioRequestDto(SQLAlchemyAutoSchema):
  # pasar atributos a la clase que estamos heredando (SQLAlchemyAutoSchema)
  class Meta:
    # Esta calse permitirá definir atributos necesarios para la calse que estamos heredando
    # model > estaremos indicando a SQLAlchemyAutoSchema cual serpa el modelo que tiene que utilizar para generar las validaciones necesarias
    model = UsuarioModel