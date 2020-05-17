"""
Condicionales
"""

color = 'verde'
if color == 'azul':
    print('el' + color)
elif color == 'amarillo':
    print("lo" + color)
else:  # no es necesario el else
    print("El color no es azul")
"""
Ciclos
"""

# while
numero = 12345
contador = 0

while contador < numero:
    contador += 1

print("contador", contador)

# for
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in numeros:
    print(numero)

texto = "hello world"
for letra in texto:
    print(letra)

valores = ([1, 2, 3], ("h9ola", "que", "tal"), [True, False, True])
# si se conoce la cantidad de elimenos dentro de la lista, se podran acceder mediante el for directamente a sus valores
for valor1, valor2, valor3 in valores:
    print(valor1, valor2, valor3)

# range(inicial, final -1, salto)
# range(cantidad_datos)
for valor in range(-10, 10, 2):
    print(valor)

lista = [100, 200, 300, 50, 1222, "hey", True]
# enumarate(array/rango, valor_inicial_idx)  permite generar indices a cada valor
for idx, value in enumerate(lista):
    print("Indice [%s" % (str(idx)) + "] = %s" % (str(value)))

# continue en un ciclo, hace que el ciclo de un salto a la siguiente iteracion,
# break rompe el ciclo
for valor in lista:
    if valor == 50:
        continue
    print(valor)

# asignacion ternaria, con un condicion al de una linea
calificacion = 10
color_calificacion = 'verde' if calificacion >= 1 and calificacion <= 5 else 'rojo'
print('color_calificacion', color_calificacion)
