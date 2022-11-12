from marshmallow import Schema, fields

# DTO (Data Transfer Object - Objetos de Transferencia de Datos) Manual
class PruebaDto(Schema):
  # El DTO no solamente sirve para validar la información que hemos definido, sino que ademas validará alguna información extra que no vamos a utilizar
  id = fields.Int()
  nombre = fields.Str(required=True, error_messages={'required': 'Este campo es obligatorio'})
  correo = fields.Email(error_messages={'invalid':'Correo electrónico inválido'})

