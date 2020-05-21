class Usuario:

    # la funcion __init__ permite definir los atributos de la clase, y es el constructor de la clase
    def __init__(self, fuerza=0):
        self.altura = 179
        self.peso = 76
        self.fuerza = fuerza

    # todas las funciones dentro de una clase, deben recibir un parametro
    # por convencion se coloca self, pero puede ser cualquier nombre, y este idnicara que es un metodo de clase
    def saludar(self, nombre):
        print("Holaaa ", nombre, " que tal ?")

    def mostrar_info(self):
        # para acceder a propiedades de clase, se usa => self.atributo
        print("Apellido", self.lastname)
        print("Email", self.email)

    def crear_atributos(self, direccion):
        # se puede crear atirubtos de clase dentro de la misma funcion
        self.direccion = direccion


user1 = Usuario()
# type(objeto) => devuleve de que tipo es el objeto de instancia de la clase
print(type(user1))
user1.saludar("Gustavo")

# Adicionando propiedades externas a la clase
user2 = Usuario(500)  # le pasamos la fuerza, ya que lo recibe el init "constructor"
user2.lastname = 'Marquez'
user2.email = 'ing.gstavo.marquez@gmail.com'
user2.mostrar_info()

user2.crear_atributos('Calle 57')
print('Direccion', user2.direccion)

print("Peso", user2.peso, "altura", user2.altura, "fuerza", user2.fuerza)


class Circulo:
    pi = 3.144422  # es una variable de clase

    def __init__(self, radio):
        self.radio = radio  # variable de instancia, le pertenecen a la instancia


circulo_a = Circulo(10)
circulo_b = Circulo(50)
# modificando los valores de los atributos
circulo_b.radio = 900
circulo_b.pi = 5

# Las variables de clase, no requieren de instancia
print("PI variable de clase", Circulo.pi)

print("circulo_a.radio", circulo_a.radio)
print("circulo_a.pi", circulo_a.pi)
print("circulo_b.pi", circulo_b.pi)
print("circulo_b.radio", circulo_b.radio)



"""
Metodos estaticos
"""
class Triangulo:


    numero_2 = 2
    # se decora para hacer el metodos estatico
    # se limitan a no usar variables de instancia
    @staticmethod
    def area(base, altura): # no necesita de self, com obase ya que no necesita instancia
        # puede usar variables de clase, llamando a la clase.variable
        return (base * altura) / Triangulo.numero_2

# Se llama directamente Clase.metodo_estatico
print("Area de triangulo", Triangulo.area(10,50))

"""
Metodos de clase
# similar a metodo estatico, pero permite usar variables de clase, sin llamar directamnete a la misma
"""

class Circulo2:

    pi = 3.12555
    #se decora la clase
    @classmethod
    def area(cls, radio): # por convension el primer parametro se denomina cls, n params
        # con el cls.variable accede a variables unicamente de clase mas no de instancia
        return cls.pi * radio**2
# permite acceder directamente al metodo sin instancia
print("Ara de circulo", Circulo2.area(50))

