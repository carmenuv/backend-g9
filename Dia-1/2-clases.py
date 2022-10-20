class Persona:
  estatura= 1.55
  peso= 80000
  signo= 'ARIES'

  # métodos mágicos: se reconocen por tener __ al inicio y al final del nombre del método
  def __str__(self):
    # el método str sirve para indicar que cuando se mande a llamar a la clase a imprimir se modificará la impresión predeterminada que mostraba a la ubicación de memoria por lo que se va a retornar, solamente se puede retornar str
    return 'Bienvenido a la clase Persona'

  def saludar(self):
    # self > en python en todas las funciones dentro de una clase (ahora las funciones pasan a llamarse METODOS) y para que pueda utilizar la propia configuración de la clase (como sus atributos y otros metodos) se declara como primer parámetro la palabra 'self'
    # e lparámetro self nunc ase pasará como parámetro fuera de la clase
    texto = 'Hola soy una persona y mido ' + str(self.estatura)
    print(texto)

  def saludar_cordialmente(self, nombre):
    texto = 'Hola {}, mucho gusto.'.format(nombre)
    return texto


# variable > instancia de la clase realiza una copia y todas las modificaciones que se realicen SOLO se harán en esa copia de la clase
eduardo = Persona()
gabriela = Persona()
eduardo.estatura = 1.89
gabriela.estatura = 1.75

# retorna el nombre de la clase en formato string
print(Persona.__name__)

print(eduardo)
print(eduardo.estatura)
print(gabriela.estatura)

eduardo.saludar()
gabriela.saludar()
resultado = eduardo.saludar_cordialmente('Angel')

print(resultado)