from django.contrib.auth.models import BaseUserManager
# Manager > administrador que se encargará de la creación del usuario por comando

class UsuarioManager(BaseUserManager):
  # Esta clase me servirá para indicar cómo tenemos que crear el usuario cuando se haga por línea de comandos
  def create_superuser(self, correo, nombre, apellido, tipoUsuario, password):
    # Método que se mandará a llamar cuando se ejecute el comando 'createsuperuser'
    # Los parámetros que definimos en este método SE TIENEN QUE LLAMAR IGUAL que los atributos del modelo
    if not correo:
      raise ValueError('El usuario debe indicar obligatoriamente el correo')
    # normalizo el correo > aparte de validar el patrón de correo lo que hace es remueve espacios en blanco innecesarios al inicio y al final y lo lleva todo a minúscula
    # normalize_email viene de BaseUserManager
    correoNormalizado = self.normalize_email(correo)
    # manda a llamar al modelo del usuario y crea una nueva instancia de ese usuario
    nuevoUsuario = self.model(correo=correoNormalizado, nombre=nombre, apellido=apellido, tipoUsuario=tipoUsuario)

    # generar el HASH de la contraseña para que no se guarde de manera original
    # set_password(password) genera un hash de la contraseña usando bcrypt y el algoritmo SHA256
    # https://docs.djangoproject.com/en/4.1/ref/contrib/auth/#django.contrib.auth.models.User.set_password
    nuevoUsuario.set_password(password)
    # La siguiente configuración sería si aun queremos utilizar el panel administrativo
    # is_superuser > sirve para indicar si el usurio es un usuario maestro y puede tener acceso a todo el panel administrativo
    nuevoUsuario.is_superuser = True
    # is_staff > sirve para indicar si el usuario pertenece al equipo de trabajo y puede tener acceso al panel administrativo (el if_staff estará regido por los permisos que puede tener ese usuario)
    nuevoUsuario.is_staff = True
    # Sirve para referenciar a la base de datos por default en el caso que tengamos varias conexiones a diferentes base de datos
    # de momento el self._db estará vacío por lo que usará la conexion a la base de datos por defecto, caso contrario si tuviésemos más de una conexión a alguna bd entonces indicariamos a que bd queremos conectarnos
    nuevoUsuario.save(using=self.db)