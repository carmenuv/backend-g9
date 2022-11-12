def prueba(**argumentos):
  print(argumentos)

prueba(nombre='eduardo', apellido='de rivero')

persona = {
  'nombre':'eduardo',
  'apellido':'de rivero'
}

prueba(persona=persona)

# Cuando nosotros en una función pasamos un DICCIONARIO pero con doble asterisco antes (**) que sacará las llaves (keys) y lo colocará como parámetro de la función y sus valores como los valores de esos parámetros
prueba(**persona)
prueba(nombre=persona['nombre'], apellido=persona['apellido'])

# Si usamos una función con parámetros definidos entonces tenemos que indicar en el diccionario ESE MISMO NOMBRE DE PARÁMETROS ya que si si es diferente, arrojará un error
def saludar(nombre, apellido):
  print(nombre, apellido)

usuario = {
  'nombre': 'eduardo',
}

usuario2 = {
  'nombrecito': 'juanito'
}

saludar(**usuario)
#Esto me arrojará un error ya que el parámetro 'nombrecito' no concuerda con el paráemtro esperado (nombre)
saludar(**usuario2)
saludar(nombrecito='pedrito')