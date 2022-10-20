#Operadors artméticos
numero1, numero2 = 10, 50

#SUMA
#Nota: solamente será suma si la sdos variables son numéricas, si son strings entonces se hará una concatenación y además no se puede sumar entre string y numéros
print(numero1 + numero2)

#RESTA
#Nota: solamente para números
print(numero1 - numero2)
# print('ab' - 'bc')

#MULTIPLICACIÓN
#Nota: si se usa la multiplicación en un string, entonces este repetirá el número de veces entre un string y un número de veces
print(numero1 * numero2)
print('hola'*5)

#DIVISIÓN
#Nota, siempre me devolverá un float (número flotante)
print(numero1 / numero2)

#MÓDULO
#el resultado de la división netera (sin parte decimal)
print(numero1 % numero2)

#COCIENTE
#el cociente entero
print(numero1 // numero2)


#EXPONENTE
#10^50
print(numero1 ** numero2)

#RAIZ CUADRADA usando exponente
print(numero1 ** 0.5)


# -----------------------------------
# OPERADORES DE ASIGNACIÓN
#Igual asignar un nuevo valor a una variable
numero1 = 100

#INCREMENTO
numero1 += 1 #Incrementando el valor del numero1 en una unidad
print(numero1)

#DECREMENTO
numero1 -= 1 # numero1 = numero1 - 1
print(numero1)

#MULTIPLICADOR
numero1 *= 2
print(numero1)

#DIVIDENDO
numero1 /= 5 


# -----------------------------------
# OPERADORES DE COMPARACIÓN siempre retornarán un booleano (Si es verdadero o si es falso)
# IGUAL QUE
# Nota: En Python, a diferencia de javascript, no existe el triple igual (Comparador de tipo de datos)
print(numero1) #flotante
print(numero2) # int
print(numero1 == numero2)
print(int(40.7)) #asi se convierte el tipo de dato a entero
#int('carmen') # no se puede convertir tipos de datos irreales
print(type(numero1) == type(numero2))

# MAYOR | MAYOR O IGUAL
print(10 > 9.58)
print(10 > int('5'))
print(50 >= 50)

#MENOR | MENOR O IGUAL
print(50 < 80)
print(50 <= 50)
#Nota: siempre va el símbolo de mayor(>) o menor (<) antes del igual, nunva al revés porque sino python entiende que s está tratando de una asignación


# ------------------------------------
# OPERADORES LÓGICOS
# Sirve para comparar vaias condicionales
# && paa indcar un AND, en python se usa la palabra and
# || para indicar un OR, en python se usa la palabra or

# and > TODAS las ocndiciones tienen que ser verdaderas para que todo sea verdadero

eduardo=30
ronald=25
henry=25
carmen=19
angel=15

print((angel > eduardo) and (ronald < henry))
print((eduardo > angel) and (carmen < ronald))

# or > AL MENOS una condición tiene que ser verdadera para que todo sea verdadero
print((carmen > ronald) or (eduardo > ronald))

# OPERADORES DE CONTENIDO
verduras = ['apio', 'rocoto', 'zanahoria']

print('tomate cherry' in verduras)
print('champiñon' not in verduras)