from flask import Flask, request
# request > toda la información que puedo leer del usuario, dentro de ella tendremos el body
from datetime import datetime
from flask_cors import CORS

usuarios = [{
  'correo': 'carmenurizarv@gmail.com',
  'nombre': 'Carmen',
  'apellido': 'Urízar'
}]


# __name__ > variable propia de python, muestra si el archivo es el archivo principal del proyecto, mostrará el valor de '__main__' y si no entonces mostrará otro valor
print(__name__)
app = Flask(__name__)
# DECLARAR LOS CORS (Intercambio de recursos de orrigen compartido)
CORS(app)

#decorador
# Endpoint > es cuando definimos una ruta para que pueda ser accedida
# Si no se define qué verbo HTTP puede acceder, entonces el valor por defecto será GET 
@app.route('/', methods = ['GET'])
def inicio():
  # Controlador (CController) > La funcionabilidad que tendrá mi endpoint
  print('ingresó al endpoint inicial')
  # Siempre en todo controlador hay que retornar algo
  return 'Bienvenido a mi primera API en Flask semana 2'

@app.route('/estado', methods= ['GET'])
def estado():
  hora_servidor = datetime.now().strftime('%I:%M:%S %p')
  return {
    'estado': True,
    'hora': hora_servidor
  }

@app.route('/registrarse', methods=['POST'])
def registro():
  # request.data > nos devuelve el body pero en formato puro(formato bytes)
  print(request.data)
  # request.get_json() > convierte la información entrante en un diccionario para que pueda ser utilizado sin problemas en python
  print(request.get_json())
  body = request.get_json()
  #iterar el arreglo de usuarios y validar que no exista un usuario con ese correo proveniente del body
  for usuario in usuarios:
    print(usuario)
    correo = usuario.get('correo')
    if correo == body.get('correo'):
      return {
        'message': 'El usuario ya está registrado'
      }

  # cómo extraer l ainformación de un diccionario
  # body.get('correo')
  # body['correo']

  usuarios.append(body)
  # si no existe entonces agregar ese usuario al arreglo, caso contrario, retornar un mensaje que diga que el usuario ya está registrado
  return {
    'message': 'Usuario registrado exitosamente'
  }

# crear un endpoint que sea '/listar-usuarios' y este devolverá el siguiente resultado
# { message: 'Los usuarios son', conten:. [{...}, {...}]}

@app.route('/listar-usuarios', methods = ['GET'])
def listarusuarios():
  return {
        'message': 'Los usuarios son',
        'content': usuarios
      }


# run > sirve para correr nuestro servidor en modo de desarrollo
# si declaramos algo después del método run este nunca se llamará porque eaca se queda 'pegado' esperando peticiones del cliente
# debug > indicará si guardamos algún archivo dentro del proyecto reiniciará automáticamente el servidor
app.run(debug=True)

