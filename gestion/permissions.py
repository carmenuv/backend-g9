from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.request import Request

class SoloAdmin(BasePermission):
  # Si queremos cambiar el mensaje de respuesta cuando falle la validación:
  message = 'Tu no tienes los permisos necesarios'


  def has_permission(self, request:Request, view):
    # view > es la vista a la cual se está tratando de acceder
    # SAFE_METHODS > es un listado en el cual me muetra los metodos seguros (los que no afectan la modificaicón de datos (GET, OPTIONS, HEAD))
    print(SAFE_METHODS)
    if request.method in SAFE_METHODS:
      # si el metodo que está utilizando para acceder es GET | OPTIONS | HEAD
      return True
      
    print(request.user)
    print(view)
    if request.user.tipoUsuario == 'ADMIN':
      return True
    else:
      return False