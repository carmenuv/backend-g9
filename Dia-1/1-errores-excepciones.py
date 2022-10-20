#El try va de la mano con el except, no pueden ir separados

try:
  #Si no se emite ningún error dentro del try JAMÁS ingresará al except
  # print(10/0)
  int('a')
except ZeroDivisionError:
  #Aquí ingresará si el error es de tipo ZeroDivisionError
  print('Hubo un error al dividir entre cero')
except ValueError:
  # Aca entrará si hubo un error de conversión a entero
  print('Error al convertir el número')
except Exception as error:
  # Aca entrará si el error es otro genérico
  # .args > es el atributo de toda instancia de Exception que me devolverá el porqué se dio ese error(argumentos)
  print(error.args)
  print('Hubo un error al dividir entre cero')

print('Yo no soy un error')

try:
  #args son los argumentos que nosotros indicaemos o que recibiremos cuando se de un error, en este atributo se podrán obtener todos los argumentos del porqué se deio ese error
  raise Exception('eres menor de edad', 'no eres peruano', 'no eres femenino') #throw new Error() > JS | raise sirve para disparar ese error
except Exception as error:
  print(error.args)


try:
  resultado = 5/1
  raise Exception('Error desconocido')

except Exception as error:
  print(error.args)

else:
  #en el caso que el código se ejecutase sin nigún error (sin ingresar al except)
  print('La operación se realizó exitosamente')

finally:
  #si la ejecución estuvo bien o si ingresó al except
  print('Si la operación estuvo bien o mal igual se ejecuta')


#EJERCICIO:
#Recibir por el teclado un número

numero = input('Ingresa un número: ')

try:
  numeroEntero = int(numero)
except ValueError:
  print('El valor ingresado es incorrecto')
else:
  print(numeroEntero + 10)


#tratar de convertir ese número a un entero (si no se puede, indicar que el valor es incorrecto). Sumar 10 + ese número ingresado y devolver
