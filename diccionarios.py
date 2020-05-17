diccionario1 = {
    "nombre": "Gustavo",
    "apellido": "Marquez",
    "edad": 24,
    "telefonos": {
        "casa": 75555,
        "celular": 333333
    }
}
# se puede acceder o crear a una posicion/llave
diccionario1["localidad"] = "bosa"
print(diccionario1)

isCiudadInDiccionario1 = "ciudad" in diccionario1  # pregunta si se encuentra la llave ciudad en el diccionario
print("isCiudadInDiccionario1", isCiudadInDiccionario1)

# .get(llave, valor_llave_si_no_Existe)   # Recomendada para obtener los datos de un diccionario
print('diccionario1.get("nombre")', diccionario1.get("nombre"))

# .setdefault(llave, valor_llave_si_no_Existe)  # si no encunetra la llave la crea pusheandola en el diccionario inicial
resultado_llave = diccionario1.setdefault('pais', 'colombia')
print(resultado_llave)
# .keys() devuelve las llaves del diccionario
get_llaves_diccionario1 = diccionario1.keys()
print('get_llaves_diccionario1', list(get_llaves_diccionario1))
# .values() devuelve los valores del diccionari
get_values_diccionario1 = diccionario1.values()
print('get_values_diccionario1', get_values_diccionario1)
# .items() devuelve en parejas los items del ddiccionario (key, value)
items_diccionario1 = diccionario1.items()
print('items_diccionario1', items_diccionario1)

# del permite eliminar una llave de un diccionario
del diccionario1['telefonos']
# .pop(llave)  elimina la llave y valor de un diccionario
diccionario1.pop("pais")
print("diccionario1 eliminando telefonos y pais", diccionario1)
diccionario1.clear()   # .clear() vacia el diccionario
print(diccionario1)