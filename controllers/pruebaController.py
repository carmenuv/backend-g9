from flask_restful import Resource, request
from marshmallow.exceptions import ValidationError
from dtos.prueba import PruebaDto

class PruebaController(Resource):
  def post(self):
    try:
      data= request.get_json()
      validador = PruebaDto()
      # cargar la información a validar
      dataValidada = validador.load(data)
      print(dataValidada)

      return{
        'message': 'ok'
      }
    # Si al momento de hacer la validación de nuestro DTO falla algún atributo entonces el propio marshmallow emitirá un eror que lo podremos capturar mediante el except de ValidationError
    except ValidationError as error:
      # args > el atributo donde se almacenará toda la descripción de los errores
      return {
        'message': 'Error al hacer la consulta',
        'content': error.args
      }