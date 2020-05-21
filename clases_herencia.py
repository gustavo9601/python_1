"""
Todas las clases heredan de la clase object
Ambas heredan =>
class Animal(object)
class Animal
"""


# clase padre
class Animal:
    def comer(self):
        print("Comiendo")

    def dormir(self):
        print("Durmiendo")


class Mascota:

    def fecha_adopcion(self, fecha):
        self.fecha_de_adopcion = fecha
        print("La fecha de adopcion es ", self.fecha_de_adopcion)


# clase hijo
# class nombreClaseHijo(nombreClasePadre, nClasesPadres)  de esta forma puede heredar las funciones del padre
class Perro(Animal, Mascota):
    def __init__(self, nombre):
        self.nombre = nombre

    def ladrar(self):
        print("El perro " + self.nombre + " ladra, Guagu guagu")


perro1 = Perro("Firulais")
perro1.comer()
perro1.dormir()  # metodo heredado
perro1.ladrar()  # metodo heredado
perro1.fecha_adopcion('Hoy')

"""
Metodos propios de la clase object 
"""


class Pato:

    def __init__(self, nombre):
        self.nombre = nombre
        self.size = 24

    # este metodo permite modificar la salida al impirmir solo el objeto de instancia
    def __str__(self):
        return "Modificando el comportamiento del metodo __str__ " + self.nombre


pato1 = Pato("Donald")
print("pato1", pato1)
# __dict__ permite visualizar los atributos de instancia de la clase
print("pato1.__dict__", pato1.__dict__)

