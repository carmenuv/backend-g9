# LISTAS
# Colecciones de datos ORDENADAS y modificables

nombre = ['Angel', 'Carmen', 'Sofia', 'Adolfo', 'Henry', 'Felipe']

#Las listas pueden contener diferentes tipos de datos
miscelaneo = ['Jueves', 13, 'Soleado', False, [1,2,3]]

#podemos acceder a su contenido mediante las posiciones
print(nombre[0])

#longitud > cantidad de elementos que hay en esa colección
# posición > ubicación de un elemento determinado, que siempre empieza en 0
# len() > devuelve el número de items de un contenedor, puede ser un string (y retornará los caracteres) o una colección de datos y retornará los items

print(len('nombre'))
longitud = len(nombre)
print(nombre[longitud - 1])

# L aúltima posición de la lista
print(nombre[-1])
print(nombre[-2])

#Desde la posición 1 hasta la posición menor que 4
print(nombre[1:4])
#Desde l aposición 1 hasta el final
print(nombre[1:])
#Desde el inicio hasta menor que 5
print(nombre[:5])
#Copia el contenido de un arregelo (colocando en otra posición de memoria)
print(nombre[:])
print(id(nombre))
alumnos_lima = nombre[:]
print(id(alumnos_lima))
#Si cambiamos el contenido de una posición de memoria, agregamos o eliminamos el contenido se verá reflejado tanto en la variable original como en l variable huesped
print(alumnos_lima)
nombre[0] = 'Felix'
#Si cambiamos el contenido de la variable AHI RECIÉN la variable huesped 'alumnos_lima' cambiará su ubicación en la memoria
# nombre = 'hola mundo'
print(alumnos_lima)





#Mostrar solo a Angel y Carmen, luego Mostrar a Adolfo, Henry y Felipe y luego concatenar las dos listas
print(nombre[:2] + nombre[3:])

#agregar un nuevo elemento a la lista
nombre.append('Juan Pablo')
print(nombre)

#Eliminar(extrae) según el índice
alumno_eliminado = nombre.pop(0)
print(alumno_eliminado)
print(nombre)

#remove(valor) > si no existe el valor emitirá un error, si si existe, lo eliminará, no devuelve nada
#aquí estamos extrayendo a Adolfo y lo estamos guardando en alumno_eliminado2 por eso devuelve none
alumno_eliminado2 = nombre.remove('Adolfo')
print(nombre)
print(alumno_eliminado2)

#del elimina la posición (muy parecido al pop pero no devuelve nada)
del nombre[0]
print(nombre)

#Limpiar por completo la lista
nombre.clear()
print(nombre)

#para más información https://docs.python.org/3/tutorial/datastructures.html


#---------------------------
# Tuplas
# Son ordenadas PERO no se pueden modificar (una vez definidas no se pueden alterar)

cursos = ('backend', 'frontend')
mix = (1, 80.2, False, 'Eduardo', (1,2,3))

print(cursos[0])
print(cursos[:1])

#no se puede agregar
#cursos.append('design')

#ni editar
# cursos[0] = 'mobile'

#ni eiminar
#del cursos[0]

print(cursos)
print(len(cursos))


# ---------------------------
# Conjunto (Set)
# Colección de datos DESORDENADA una vez creada ya no se puede acceder mediante asus posiciones

primos = {1, 3, 5, 7, 11, 13, 17, 19}
estaciones = {'verano', 'otoño', 'primavera', 'invierno'}

print(estaciones)
print(17 in primos)

#se puede agregar nuevos elementos a un set
primos.add(23)
print(print)

#se puede eliminar sin darle una posición porque son desordenados
primos.pop()
print(primos)


# ---------------------------
# DICCIONARIOS
# Una colección ORDENADA PERO por llaves (no por índice) y editable

persona = {
  'nombre': 'Carmen',
  'apellido': 'Urízar',
  'correo': 'carmenurizarv@gmail.com',
  'telefono': '965101773'
}

#El segundo parámetro se imprime en lugar del primero si es que este no existiera
print(persona['nombre'])

#Tratará de devolver e contenido de esa llave, si no existe, retornará None o lo qu se defina en el segundo parámetro
print(persona.get('direccion', 'No hay'))

#Devuele una lista con todas las llaves del diccionario
print(persona.keys())
#Devuelve una lista con todos los valores
print(persona.values())

persona['direccion'] = 'Calle los Ruiseñores 1070A'
print(persona)

#Remueve el valor de esa llave y la elimina y opcionalmente podemos almacenar el valor en otra variable
correo_eliminado = persona.pop('correo')
print(persona)
print(correo_eliminado)

#para más info https://docs.python.org/3/tutorial/datastructures.html#dictionaries
