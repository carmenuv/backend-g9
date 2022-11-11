from marshmallow import Schema, fields

# DTO (Data Transfer Object - Objetos de Transferencia de Datos) Manual
class PruebaDto(Schema):
  id = fields.Int()
  nombre = fields.Str(required=True, error_messages={'required': 'Este campo es obligatorio'})
  correo = fields.Email(error_messages={'invalid':'Correo electrónico inválido'})

