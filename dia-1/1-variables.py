#Esto es un comentario
edad = 30

nombre = 'Carmen'
apellido = "Urízar"

#No se puede usar los backstips (comillas invertidas) para los string
#saludo  = `Hola como están mi nombre es ${nombe}`

mensaje = '''El día de hoy
empezó el módulo de
backend'''

despedida = """El día de hoy
nos despedimos hasta una nueva
oportunidad"""

lastname = "O'neil"

print(nombre)

#En python no hay ni null ni undefined ni NaN (Not A Number) todo ello se resume en None
especialidad = None
print(especialidad)

#No hay validaciones al momento de cambiar el tipo de dato
lastname = 80
lastname = None

# type(var) > devolverá qué tipo de dato es esa variable
print(type(nombre))
print(type(edad))

#También se puede declarar varias variables en una misma línea
curso, grupo, mes, dia, nota = 'CodiGo', 'Backend', 'Octubre', 10, 15.4
print(grupo)

#id(var) > mostrar la posición de memoria en la cual se está alojando la variable, función, clase, etc
print(id(curso))

#del > elimina variable (libera la memoria), no se puede volver a utilizar esa variable nunca más
del curso

print(curso)