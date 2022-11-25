from .models import UsuarioModel, PlatoModel
from rest_framework import serializers

class UsuarioSerializer(serializers.ModelSerializer):
  def save(self):
    # es el que se encarga de guardar el registro en la base de datos
    # 1. crea la instancia de nuestro nuevo usuario

    # self.validated_data = {
    #   'nombre': 'Eduardo',
    #   'apellido': 'de Rivero',
    #   # ...
    # }
    # nuevoUusario = UsuarioModel(
    #   nombre = self.validated_data.get('nombre'),
    #   apellido = self.validated_data.get('apellido')
    # )
    nuevoUsuario = UsuarioModel(**self.validated_data)

    # 2. genero el hash de la password
    nuevoUsuario.set_password(self.validated_data.get('password'))

    # 3. guardamos el usuario en la base de datos
    nuevoUsuario.save()

    return nuevoUsuario

  class Meta:
    fields = '__all__'
    model = UsuarioModel
    # https://www.django-rest-framework.org/api-guide/serializers/#additional-keyword-arguments
    # Definimos un nuevo atributo llamado extra_kwargs en el cual sse realiza mediante un diccionario y se utiliza para indicar parametros adicionales a nuestras columnas

    extra_kwargs = {
      'password': {
        'write_only': True
      },
      'id': {
        'read_only': True
      }
    }
    # Con la anterior configuración estamos indicando que el atributo 'password' solamente será para escribir más no para devolver (read) y mientras que el 'id' será solamente para la lectura, más nunca se podrá utilizar para la escritura (write)

class PlatoSerializer(serializers.ModelSerializer):
  class Meta:
    model = PlatoModel
    fields = '__all__'
    # utilizando el atributo extra_kwargs indicar que solamente la disponibilidad será de solo lectura

    extra_kwargs = {
      'disponibilidad': {
        'read_only': True
      }
    }