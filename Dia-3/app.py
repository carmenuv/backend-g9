from  flask import Flask
from config import conexion

app = Flask(__name__)
# Formato para las cademas de conexion de las base de datos:
# dialecto://username:password@host:port/database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/flask_sqlalchemy'

# configuro mi conexión de sqlalchemy con l aaplicación de flask
conexion.init_app(app)

# indicaremos la creación de las nuevs tablas que no se encuentren registradas en la bse de datos PERO esos modelos tiene que ser utilizado en el proyecto para que se pueda crear la tabla en la bd, emitirá un error si no se logró conectar a la base de datos
conexion.create_all(app=app)

app.run(debug=True)