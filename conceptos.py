
"""
Variables
Listas
Tuplas
Funciones basicas de listas
"""

# Mensaje por consola
from builtins import print

print("Hellow World this is the start of a best program in inteligence artificial")

# Variables
CONSTANTE = 1  # En py no existen constantes, por lo cual para identificarlas se pueden usar en Mayus
number1 = 1
number2 = 5
suma = number1 + number2
print(suma)

# Declaracion de variables en una misma linea, con su inicialiacion en el mismo orden de posicion
valor1, valor2, valor3 = 1, 5, 15
print(valor1, valor2, valor3)

# Operadores
print(valor1 == valor2 or valor3 > valor1)
print(True and True and True)
print(not True)  # not variable   => negacion
print(valor1 is valor1)  # is => una igualacion

# Caputar valor por teclado
print("Digita tu nombre:")
nombre = input()
print("Hola", nombre)

edad = int(input("Cual es tu edad?\n"))  # int(variable)  => parseamos a entero el valor  #\n salto de linea
# float()
print("Edad", edad)

"""
Comentarios de varias lineas
1
2
"""

# listas
lista1 = [1, 2, 3, True, False, 'hola', 'mundo', True, 'cool', 'php']
print(lista1)
print(lista1[2])
print(lista1[:])  # [:]  toda la lista
print(lista1[:6])  # [desde el princio hasta : posicion final]
print(lista1[1:])  # [posicion inicial : hasta el final]
print(lista1[1:4])  # [posicion inicial:posicion final]
print(lista1[1:6:2])  # [posicion inicial:posicion final:saltos]
print(lista1[::-1])  # [::-1] inverso de lista

lista2 = [1, 2, 3, 100, 100, 4, 2.5, 1.32]
lista2.sort()
print('lista ordenada', lista2)
lista2.sort(reverse=True)  # .sort(reverse)  ordena descendentemente
print('lista ordenada descendetemente', lista2)

print('menor de la lista', min(lista2))  # min(lista) el menor
print('mayor de la lista', max(lista2))  # max(lista) el mayor
print('Longitud de la lista', len(lista2))  # len(lista) cantidad elementos

lista2.append(10)  # insertando el 10 al final
# lista2.clear()   .clear()  vacia la lista
print(lista2)
resultado = 10 in lista2  # valor in lista  // permite preguntar si el valor esta en la lista
print('Esta el 10 en la lista?', resultado)
print('indice del valor 100', lista2.index(100))  # .index(valor)  retorna la posicion del valor a encontrar
print('cantidad de veces que se encuentra el 100', lista2.count(100))

# Matriz
matriz1 = [
    [1, 2, 3],
    [2, 8, 3]
]
print(matriz1)
print(matriz1[1][1])  # [x][y]

# Tuplas
# listas no inmutables, pero mas rapidas de acceder
tupla1 = (1, 2, 3)
print(tupla1)
print(tupla1[1])

tupla2, tupla3, tupla4 = (1, 2, 3), (4.5, 5.2), (1, 90, 2, 4, 5, 222, 666, 33)
print(tupla2)

# asingnacion lineal desacoplada
uno, dos, tres = tupla2
print(uno, dos, tres)
# con el *variable, asigna todos los valores restantes de la lista/tupla a la variable con el *
cuatro, *cinco = tupla4
print(cuatro, cinco)

listaA = [50, 20, 14, 3]
listaB = [100, 5, 50, 20, 14, 3]
listaZip = zip(listaA, listaB)  # acopla en agrupaciones (n cantidad de listas/tuplas), la misma posicion de cada arreglo
listaZip = list(listaZip)  # list()   tuple()  permiter parsear los datos
print(listaZip)
