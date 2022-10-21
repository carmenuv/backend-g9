def sumar(num1, num2, num3):
  return num1 + num2 + num3

def sumar_n_numeros(*args):
  # args > arguments será recibir N (ilimitado) número de parámetros
  print(args)
  # sumar todos los valores de la tupla args utilizando un for
  suma = 0
  for numero in args:
    suma += numero
  return suma

print(sumar(5, 10, 7))

resultado = sumar_n_numeros(10,5,18,7,22,56,89)
print(resultado)

def filtro(**kwargs):
  #kwargs > keyword argument > recibiremos u numero ilimitado de parametros pero utilizando el nombre del parametro y su valor
  print(kwargs)
  for llave in kwargs.keys():
    print(llave)
    valor = kwargs.get(llave)
    print(llave, ':', valor)

filtro(nombre='carmen', edad=29, sexo='F')
filtro(nombre='carmen', sexo='F', nacionalidad='PERUANA')

curso = {
  'nombre':'matematica',
  'dificultad': 'intermedio',
  'experiencia': 'ninguna',
  0: 'hola'
}
print(curso)
print(curso.keys())
print(curso.values())
print(curso[0])
print(curso['dificultad'])
print(curso.get('calificacion'))
print(curso.get('nombre', 'no hay'))
# modificar valores en mi diccionario, si esa llave no existe, entonces se creará
curso['mas_info'] = 'esta es una información adicional'

#metodo .get SOLAMENTE sirve para visualizar la información, más no para asignación
# curso.get('otra_info') = 'esta es otra información'