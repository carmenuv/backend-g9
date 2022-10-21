class Usuario:
  def __init__(self, nombre, apellido, correo):
    self.nombre = nombre
    self.apellido = apellido
    self.correo = correo

  def mostrar_resumen(self):
    return {
      'nombre': self.nombre,
      'apellido': self.apellido,
      'correo': self.correo
    }

class Alumno(Usuario):
  def __init__(self, correo, apellido, nombre, telefono_emergencia):
    self.telefono_emergencia = telefono_emergencia
    #el método super nos permite referenciar el constructor del padre
    super().__init__(nombre, apellido, correo)

  def saludar(self):
    print('Hola yo soy la clase alumno y el nombre es {}'.format(self.nombre))

  def mostrar_resumen(self):
    #polimorfismo > poli > muchas | morfa > formas o muchos significados
    #la forma en la cual un método dependiendo de donde se utilice va a trabajar de una manera u otra
    resumen = super().mostrar_resumen()
    resumen['telefono_emergencia'] = self.telefono_emergencia
    return resumen

    return {
      'telefono_emergencia': self.telefono_emergencia
    }

usuario01 = Usuario(nombre='Carmen', apellido='Urízar', correo='carmenurizarv@gmail.com')
usuario02 = Usuario('Milka', 'Valdivia', 'milkavaldivia@gmail.com')
usuario03 = Usuario(correo='raulurizar@gmail.com', apellido='Urízar', nombre='Raul')

print(usuario01.mostrar_resumen())

alumno01 = Alumno('jmartinez@yahoo.es', 'Martinez','Juan', '965101773')
alumno01.saludar()
print(alumno01.mostrar_resumen())