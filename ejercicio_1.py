"""
Listar todos los números pares del 0 al 100
"""

for valor in range(0, 101):
    if valor % 2 == 0 and valor != 0:
        print(valor)

"""
Eliminar todas las vocales de una frase dado por el usuario y
mostrar el nuevo string en pantalla.
"""

frase = input("Digite una frase : ")
vocales = "aeiou"

frase_array = list(frase)

for vocal in vocales:
    if vocal in frase_array:
        frase_array.remove(vocal)

frase_string = "".join(frase_array)
print("frase sin vocales", frase_string)

"""
Mostrar en pantalla la cantidad de vocales que existe en una
frase dada por el usuario.

Mostrar en pantalla la frecuencia de aparición de vocales en una
frase dada por el usuario.
"""
frase = input("Digite una frase : ")
vocales = "aeiou"

for vocal in vocales:
    if frase.count(vocal) > 0:
        print("Vocal [" + vocal + "] = " + str(frase.count(vocal)))

"""
Mostrar en pantalla la palabra que más se repita junto con la
cantidad de veces que lo hace del capituló número uno de
Frankenstein
"""

text = """
You will rejoice to hear that no disaster has accompanied the
commencement of an enterprise which you have regarded with such
evil forebodings.  I arrived here yesterday, and my first task is
to assure my dear sister of my welfare and increasing confidence in
the success of my undertaking.
; the motion is pleasant, and,
in my opinion, far more agreeable than that of an English stagecoach.
The cold is not excessive, if you are wrapped in furs--a dress which
I have already adopted, for there is a great difference between walking
the deck and remaining seated motionless for hours, when no exercise
R.  Walton
"""
text_array = text.split(" ")
diccionario_palabras = {}
for palabra in text_array:
    diccionario_palabras.setdefault(palabra, text.count(palabra))

diccionario_palabras.pop('')  # descartamos los vacios
cantidad_veces_repetidas = max(diccionario_palabras.values())

for palabra in diccionario_palabras:
    if diccionario_palabras[palabra] == cantidad_veces_repetidas:
        print("La palabra que mas se repite es [%s" % (palabra), "] y se repite %s" % (str(cantidad_veces_repetidas)))
        break

"""
Remplazar cada letra de una frase dada por el usuario por la
posición que le corresponde en el abecedario y mostrar el nuevo
string en pantalla. (Los espacios no se remplazan)
"""

frase = input("Digite la frase : ")
frase_replace = frase

abcedario = "abcdefghijklmnopqrstuvwxyz"

for letra in frase:
    posicion_letra_abc = abcedario.find(letra)
    frase = frase_replace
    frase_replace = frase.replace(letra, str(posicion_letra_abc))

print("Frase cambiada a la posicion del abc", frase_replace)

"""
Dado un diccionario, el cual almacena las calificaciones de un
alumno, siendo las llaves los nombres de las materia y los valores
las calificación, mostrar en pantalla el promedio del alumno.
"""

calificaciones = {
    "matematicas": 5.0,
    "español": 4.1,
    "ingles": 3.1,
    "programacion": 5.0
}

sumatoria_notas = 0
promedio = 0
for calificacion in calificaciones:
    sumatoria_notas += calificaciones[calificacion]

promedio = sumatoria_notas / len(calificaciones)
print('promedio_calificaciones', promedio)

"""
A partir del diccionario del ejercicio anterior, mostrar en pantalla
la materia con mejor promedio.
"""
print('calificacion_mas_alta', max(calificaciones))

"""
Crear una lista la cual almacene 10 números positivos ingresados
por el usuario, mostrar en pantalla: la suma de todos los
números, el promedio, el número mayor y el número menor.
"""
numeros = []

for idx, numero in enumerate(range(1, 10)):
    numeros.append(int(input("Numero en la posicion [" + str(idx) + '] = ')))

print("suma numeros", sum(numeros))
print("mayor de numeros", max(numeros))
print("menor de numeros", min(numeros))
print("promedio de numeros", sum(numeros) / len(numeros))

"""
Dado una lista de frases ingresadas por el usuario, mostrar en
pantalla todas aquellas que sean palíndromo.
"""

palabras = []

for idx, palabra in enumerate(range(1, 3)):
    palabras.append(input("Palabra en la posicion [" + str(idx) + '] = '))

for palabra in palabras:
    if palabra == palabra[::-1]:
        print("Palabra palindroma", palabra)
