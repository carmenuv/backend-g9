from django.db import models
# contrib > contributions
# auth_user se encuentra en la aplicación de auth
# AbstractBaseUser > me permite total control sobre la tabla 'auth_user'
# AbstractUser > me permite control solamente en las columnas de nombre, apellido, correo y password de la tabla 'auth_user'
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .authManager import UsuarioManager

# Create your models here.
class PlatoModel(models.Model):
  id = models.AutoField(primary_key=True, null=False, unique=True)
  nombre = models.CharField(max_length=50, null=False)
  # FloatField > se utiliza un tipo de dato nativo de python que seria el float
  precio = models.DecimalField(null=False, max_digits=5, decimal_places=1)
  disponibilidad = models.BooleanField(default=True)
  # auto_now_add > datetime y sirve para indicar que se guarde la hora y fecha actual del servidor cuando se cree un nuevo registro
  # https://docs.djangoproject.com/en/4.1/ref/models/fields/#datefield
  fechaCreacion = models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')

  class Meta:
    db_table = 'platos'
    # ordenar por el precio descendiente
    ordering = ['-precio']

class UsuarioModel(AbstractBaseUser, PermissionsMixin):
  # PermissionsMixin > Me sirve para poder modificar los permisos que tendrá este usuario al momento de crearse por los comandos (python manage.py createsuperuser)
  id = models.AutoField(primary_key=True, unique=True)
  nombre = models.CharField(max_length=50, null=False)
  apellido = models.CharField(max_length=50, null=False)
  correo = models.EmailField(max_length=50, unique=True, null=False)
  password = models.TextField(null=True)
  tipoUsuario = models.CharField(max_length=40, choices=[
    ('ADMIN', 'ADMINISTRADOR'), 
    ('USER', 'USUARIO')
    ], db_column = 'tipo_usuario')
  
  # utilizamos los siguientes atributos si queremos seguir trabajando con el panel administrativo
  is_staff = models.BooleanField(default=False)
  # is_active > para saber si sigue activo trabajando en la empresa
  is_active = models.BooleanField(default=True)

  createdAt =models.DateTimeField(auto_now_add=True, db_column='created_at')

  objects = UsuarioManager()

  # El campo que pedirá el panel administrativo para autorizar al usuario, tiene que ser una columna que sea 'unique'
  USERNAME_FIELD = 'correo'

  # Las columnas o campos requeridos al momento de crear el usuario por la terminal, osea serán los datos solicitados, no tiene que ir el USERNAME_FIELD puesto que esté ya está implícitamnete colocado
  # Tampoco va la contraseña porque esa ya está por defecto
  REQUIRED_FIELDS = ['nombre', 'apellido', 'tipoUsuario']

  class Meta:
    db_table = 'usuarios'