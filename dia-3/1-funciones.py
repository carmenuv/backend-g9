#Funciones definidas por el usuario
def miFuncion():
  print("Hola mundo")

def suma(a, b):
  return a + b

def comprobarEdad(edad):
  if (edad >= 18):
    return 'Eres mayor de edad'
  else:
    return 'No eres mayor de edad, no puedes ingresar'
    
# edad = int(input('Ingrese su edad: '))
# print(comprobarEdad(edad))

alumnos = ['Eduardo', 'Pepe', 'Jose', 'Miguel', 'Julia', 'Raul']

def buscarNombre():
  if not 'Eduardo' in alumnos:
    return False

  return True


#Ingresar una lista de nombres (4 nombres) y que una función haga la busqueda del último nombre (5to nombre)
nombres = []

# primer_nombre = input('Ingrese el primer nombre ')
# segundo_nombre = input('Ingrese el segundo nombre ')
# tercer_nombre = input('Ingrese el tercer nombre ')
# cuarto_nombre = input('Ingrese el cuarto nombre ')

# nombres.append(primer_nombre)
# nombres.append(segundo_nombre)
# nombres.append(tercer_nombre)
# nombres.append(cuarto_nombre)

todos_los_nombres = input('Ingrese nombres separados por comas: ')

nombre_a_buscar = input('Ingrese el nombre a buscar: ')


def separarNombres(lista_nombres):
  nombres = lista_nombres.split(', ')
  return nombres

def buscarPersona(nombre):
  array_nombres = separarNombres(todos_los_nombres)

  if nombre in array_nombres:
    return '{} ha sido encontrado {}'.format(nombre, '😃')
  return f'No pudimos encontrar a {nombre}{"😢"}'

print(buscarPersona(nombre_a_buscar))






# print(buscarNombre())
