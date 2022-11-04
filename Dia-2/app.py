from flask import Flask, render_template
from flask_mysqldb import MySQL
# me permite utilizar todas las variables del entorno y del servidor, motivos de seguridad, no expone datos sensibles.
from os import environ
# Sirve para leer el archivo .env y cargar las variables definidas en ese archivo como variables de entorno.
from dotenv import load_dotenv

load_dotenv()
# print(environ)

app = Flask(__name__)

# NOTA. Todas las variables de entorno SIEMRPE serán string
# Almacena todas las variables de configuración de la aplicación de Flask
app.config['MYSQL_HOST'] = environ.get('MYSQL_HOST') # None
app.config['MYSQL_USER'] = environ.get('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = environ.get('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = environ.get('MYSQL_DB')
app.config['MYSQL_PORT'] = int(environ.get('MYSQL_PORT'))

# print(app.config)
mysql = MySQL(app)

# Un decorador es la forma en al cual nosotros podemos modificar el comportamiento de un metodo de una clase sin la necesidad de modificarlo directamente, es como utilizar la herencia para poder modificar su comportamiento, en este caso dependiendo de su ruta y su metodo.

@app.route('/', methods=['GET'])
def inicio():
  return{
    'message': 'Bienvenido a mi API de colegios'
  }

@app.route('/inicio', methods=['GET'])
def pagina_inicial():
  return render_template('inicio.html')

@app.route('/mostrar-alumnos', methods=['GET'])
def devolver_alumnos():
  # me crea una conexión con la base de datos
  cursor = mysql.connection.cursor()
  # Ejecutamos una clausula hacia una determinada tabla
  cursor.execute("SELECT * FROM alumnos")
  resultado = cursor.fetchall()
  # Devuelve toda la información de esa consulta
  print(resultado)
  resultado_final = []
  # Itero mi resultado de mi consulta a la bd
  for alumno in resultado:
    # Creo un diccionario para indiccar la llave de cada elemento
    alumno_diccionario = {
            'id': alumno[0],
            'nombre': alumno[1],
            'ape_paterno': alumno[2],
            'ape_materno': alumno[3],
            'correo': alumno[4],
            'num_emergencia': alumno[5],
            'curso_id': alumno[6]
    }
    print(alumno_diccionario)
    resultado_final.append(alumno_diccionario)


  # return {
  #   'message': 'Los alumnos son',
  #   'content': resultado_final
  # }
  return render_template('mostrar_alumnos.html', alumnos=resultado_final, mensaje='Hola desde flask')

@app.route('/agregar-alumno', methods=['GET'])
def agregar_alumno():
  return render_template('agregar_alumno.html')

app.run(debug=True)

