"""
Permite dentro de [] () {} agregar datos minimizando codigo
Recorrer estructuras de datos dentro de la misma de finicion de la variable [](){}
"""
# [valor_almacenar for x....]
lista1 = [x for x in range(0, 101)]
print(lista1)

# { indice:valor_almacenar  for x...  condicion_de_retorno_valor   condicion 2}
diccionario1 = {idx:x for idx, x in enumerate(range(0, 101)) if x % 2 == 0}
print(diccionario1)
