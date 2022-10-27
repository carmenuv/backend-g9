# Crear una clase llamada Persona en la cual se guarden: nombre, fecha_nacimiento, nacionaliad y dni
# Crear otra clase llamada Alumno que va a heredar la clase Persona y además va a tener sus atributos: num_seguro, num_emergencia, matriculado(boolean)
# el alumno tendrá un método llamado mostrar_datos y además otro método llamado matricular en el cual si está matriculado no se podrá matricular, caso contrario, sí.
# También tener otra calse Profesor que va a tener cta_pago y maestría (str) y el profesor puede mostrar su cta_pago y además si tiene maestría al momento de motrar la cta_pago
# indicar que se le tiene que agregar 100 soles.

class Persona:
  def __init__(self, nombre, fecha_nacimiento, nacionalidad, dni):
    self.nombre = nombre
    self.fecha_nacimiento = fecha_nacimiento
    self.nacionalidad = nacionalidad
    self.dni = dni

class Alumno(Persona):
  def __init__(self, nombre, fecha_nacimiento, nacionalidad, dni, num_seguro, num_emergencia, matriculado):
    super().__init__(nombre, fecha_nacimiento, nacionalidad, dni)
    self.num_seguro = num_seguro
    self.num_emergencia = num_emergencia
    self.matriculado = matriculado
    self.__inscritos = []
  
  def mostrar_datos(self):
    return {
      'nombre': self.nombre,
      'fecha_nacimiento': self.fecha_nacimiento,
      'nacionalidad': self.nacionalidad,
      'dni': self.dni,
      'num_seguro': self.num_seguro,
      'num_emergencia': self.num_emergencia,
    }

  def matricular(self):
    inscrito = {
      'nombre': self.nombre,
      'fecha_nacimiento': self.fecha_nacimiento,
      'nacionalidad': self.nacionalidad,
      'dni': self.dni
    }

    if (self.matriculado == True):
      print('El alumno ya fue matriculado.')
    else:
      self.__inscritos.append(inscrito)
      self.matriculado = True
      print('El alumno ha sido matriculado exitosamente.')

class Profesor:
  def __init__(self, cta_pago, maestria):
    self.cta_pago = cta_pago
    self.maestria = maestria

  def mostrar_info(self):
    print('cuenta de pago: ', self.cta_pago, 'maestria: ', self.maestria)
    if (self.maestria == 'tiene maestria'):
      print('Agregar S/.100')