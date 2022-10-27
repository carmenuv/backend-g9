# Replicar la funcionalidad de la librería CamelCase
# HINT: los strings en python son considerados listas
# texto ='eduardo' > texto[0] = 'e'...

from camelcase import CamelCase

nombre = CamelCase(input('Escribe tu nombre: '))
apellido = CamelCase(input('Escribe tu apellido: '))
correo = input('Escribe tu email: ')

def datos(nombre, apellido, correo):
  if ((nombre != '') and (apellido != '') and (correo != '')):
    return f'Te has registrado exitosamente, tus datos son: {nombre} {apellido} {correo}'
  else:
    return 'Por favor, asegúrate de llenar todos los campos.'

print(datos(nombre, apellido, correo))

texto = 'hola como estan'

class CamelCasePropia:
  def __init__(self):
    pass

  def hump(self, texto):
    nuevoTexto = texto.split(' ')
    palabrasMayus = []

    for palabra in nuevoTexto:
      # nuevoTextoMayus = nuevoTextoMayus+palabra[0].upper() + palabra[1:]' '
      print(palabra[0].upper() + palabra[1:])
      palabrasMayus.append(palabra[0].upper() + palabra[1:])
    nuevoTextoMayus = ' '.join(palabrasMayus)
    return nuevoTextoMayus

cc = CamelCasePropia()
print(cc.hump(texto))