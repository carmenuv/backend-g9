from flask_restful import Resource, request
# request, extrae información del body
from config import conexion
from models.usuarios import UsuarioModel
from dtos.usuarioDto import UsuarioRequestDto

class UsuariosController(Resource):
    # los metodos que nosotros queramos utilizar (GET, POST) lo tendremos que definir como metodo de la clase
    def get(self):
      # SELECT * FROM usuarios;
      # Me devolverá una lista con todas las instancias de la clase UsuarioModel pero las tengo que formatear para poder deovlverlas al frontned
      usuarios = conexion.session.query(UsuarioModel).all()
      

      # ------------------
      # MODO NORMAL
      # si queremos pasarle un conjunto de instancia (lista) al DTO
      serializador = UsuarioRequestDto(many=True)
      # A este método le pasamos información proveniente de la base de datos y nos los convertirá a un tipo de dato que pueda ser legible por el frontend
      # en base al modelo que estamos trabajando en ese DTO hará la conversión de tipos de datos (srt, int, float, etc)
      # el metodo dump solamnte espera recibir una instancia a la vez
      data = serializador.dump(usuarios)
      # -----------------------------------

      
      # -----------------------------------
      # MODO PRINCIPIANTE
      # hacer un for en el cual se iteren todos los usuarios y cada usuario convertirlo a un diccionario que tenga el siguiente formato
      # y luego agregarlo a la lista
    #   usuariosFinales = []
    #   for usuario in usuarios:
    #       usuarioDiccionario = {
    #         'id': usuario.id,
    #         'nombre': usuario.nombre,
    #         'correo': usuario.correo,
    #         'telefono': usuario.telefono
    #       }
    #       usuariosFinales.append(usuarioDiccionario)
        
      return {
          'message': 'Los usuarios son',
          'content': data
      }
    
    def post(self):
        body = request.get_json()
        try:
            # Instancia de mi DTO de usuario
            serializador = UsuarioRequestDto()
            dataSerializada = serializador.load(body)
            print(dataSerializada)

            # Primero creo una nueva instancia de mi clase model 
            # para mayor información mira el archivo 'repaso_funciones_infinitas.py'           
            nuevoUsuario = UsuarioModel(**dataSerializada)
            # asigno los valores a los atributos provenientes del body
            # INSERT INTO usuarios (nombre, correo, telefono) VALUES ('...', '...', '...');
            # Forma principiante
            # nuevoUsuario.correo = body.get('correo')
            # nuevoUsuario.nombre = body.get('nombre')
            # nuevoUsuario.telefono = body.get('telefono')

            # ahora agregamos a la base de datos ese nuevo registro creado en base a la instancia
            conexion.session.add(nuevoUsuario)
            # guardar de manera permanente la informacion agregada al nuevo usuario
            conexion.session.commit()

            return {
                'message': 'Usuario creado exitosamente'
            }
        except Exception as error:
            print(error)
            return {
                'message': 'Error al crear el usuario',
                'content': error.args
            }

class UsuarioController(Resource):
    def get(self, id):
        # el parámetro que nosotros indiquemos al metodo tiene que ser exactamente el mismo que hemos definido en la ruta
        # devolver un solo usuario
        # SELECT * FROM usuarios WHERE id=2 LIMIT 1;
        usuarioEncontrado = conexion.session.query(UsuarioModel).filter_by(id=id).first()
        # utilizando el UsuarioRequestDto pasarle el usuariosEncontrado y devolver esa información
        serializador = UsuarioRequestDto()
        # Esto sería sin usar el serializador
        # data = {
        # 'id': usuariosEncontrado['id'],
        # #...
        # }
        data = serializador.dump(usuarioEncontrado)
        return {
            'content': data
        }

    def put(self, id):
        try:
            # buscaré ese usuarui por el id
            usuarioEncontrado = conexion.session.query(UsuarioModel).filter_by(id=id).first()
            # si no hay un usuario con ese id
            if usuarioEncontrado is None:
                raise Exception('Usuario no existe')

            body = request.get_json()
            serializador = UsuarioRequestDto()
            data = serializador.load(body)

            # si el usuario no me envía el telefono entonces conservar el valor anterior PERO si me envía el valor 'null' ahí si le eliminamos el telefono
            telefono = usuarioEncontrado.telefono
            try:
                # Si la llave 'telefono' no existe emitira un erro por lo que ingresara al except y por ende, en este caso, no haremos nada
                telefono = data['telefono']
            except:
                pass

            # aca sobreescribimos la información nueva del usuario
            usuarioEncontrado.nombre = data.get('nombre')
            usuarioEncontrado.correo = data.get('correo')
            usuarioEncontrado.telefono = telefono

            conexion.session.commit()

            return {
                'message': 'Usuario actualizado exitosamente' 
            }

        except Exception as error:
            return {
                'message': 'Error al actualizar el usurio',
                'content': error.args
            }

    def delete(self, id):
        try:
            # buscamos el usuario
            usuarioEcontrado = conexion.session.query(UsuarioModel).filter_by(id=id).first()
            # si no hay usuario emitiremos un error
            if usuarioEcontrado is None:
                raise Exception('Usuario no existe')
            # asi eliminamo el usuario de la base de datos
            conexion.session.delete(usuarioEcontrado)
            # aquí confirmamos la eliminación de manera permanente
            conexion.session.commit()
            return {
                'message': 'El usuario se eliminó exitosamente'
            }
        except Exception as error:
            return {
                'message': 'Error al eliminar el usuario',
                'content': error.args
            }
