curso = "Curso de PY 3"

cantidad_Carateres = len(curso)
print("cantidad_Carateres", cantidad_Carateres)

# py interpreta los strings, cada caractere como una posicion de lista
# pero las posiciones son solo de consulta, no pueden mutar su valor
print('curso[2:5]', curso[2:5])
print('curso[::-1]', curso[::-1])  # ::-1  invertimos la cadena

lenguajes = "php, python, c#, java, js"
lenguajes_array = lenguajes.split(', ')  # .split('separador')  # convierte a arreglo un string
print('lenguajes_array', lenguajes_array)

lenguajes_string = " - ".join(
    lenguajes_array)  # "separador".join(arreglo)  # convierte un arreglo en string, definiendo su separador
print('lenguajes_string', lenguajes_string)

# """  empezando el string de esta forma, se pueden hacer textos multilinea
text_saltos_linea = """ 
Hola que tal
esto es un
texto """

text_saltos_linea_array = text_saltos_linea.splitlines()  # .splitlines()  permite convertir un aray separador por saltos de linea
print('text_saltos_linea_array', text_saltos_linea_array)

######################
# Modificaciones en el string
texto_inicial = " Curso de PY 3 (tres) "
print('texto_inicial.capitalize()', texto_inicial.capitalize())  # .capitalize()  primer letra en mayus
print('texto_inicial.swapcase()', texto_inicial.swapcase())  # .swapcase()  alterna de mayus a min y viseversa
print('texto_inicial.upper()', texto_inicial.upper())  # .upper()  todo a mayus
print('texto_inicial.lower()', texto_inicial.lower())  # .lower()  todo a min
print('texto_inicial.isupper()', texto_inicial.isupper())  # .isupper() devuelve si es mayus boolean
print('texto_inicial.islower()', texto_inicial.islower())  # .islower() devuelve si es min boolean

texto_inicial_title = texto_inicial.title()  # .title()  # formatea el texto como un titulo
print('texto_inicial_title', texto_inicial_title)

texto_inicial_replace = texto_inicial.replace('PY',
                                              'Python')  # .replace(varlo_buscar, valor_reemplazar) # reemplaza un valor por otro
# texto.replace(valor_buscar, valor_reemplazar, numero_veces_reemplazar)
print(texto_inicial_replace)

print('texto_inicial.strip()', texto_inicial.strip())  # .strip()  # remueve espacios en blanco al inicio y al fin

##########################
# pasando variables para strings

curso = "Python"
version = "3.0"
# " %s " %(variable)   # %s en el string indica el valor a cambiar, %(variable)   variable a cambiar
curso_Version = "Curso de %s en la version %s" % (curso, version)
print(curso_Version)
# " {} ".format(variable)  # permite indicar que ira una variable en el string   .format(variable)
curso_Version = "Curso de {} en la version {}".format(curso, version)
print(curso_Version)
# " {a} ".format(a=variable)  # de esta forma realiza el reemplazo en funcion de la variable y no d eposicion
curso_Version = "Curso de {a} en la version {b}".format(a=curso, b=version)
print(curso_Version)

##########################
# Concatenaciones
curso = "Curso de Python"
# se concatena c + [1:] la posicion 1 hasta el final   # str(numero)  al contaenar se debe parsear a string
curso = "c" + curso[1:] + " full ** " + str(3)
print("curso", curso)

##############################
# Busqueda de caracteres o palabras dentro de un string
mensaje = "Welcome to this course of python by gustavo gustavo"
cantidad_veces = mensaje.count("gustavo")
print("cantidad_veces gustavo", cantidad_veces)

text_in_mensaje = "pythons" in mensaje  # "texto" in string  # retorna booleano de sncontrar la palabra o caracter
# not in   # negando la afirmacion
print("text_in_mensaje", text_in_mensaje)

# .find("texto")   # devuleve la posicion de la primer letra, donde encuentre el texto
print("mensaje.find('python')", mensaje.find("python"))

busqueda = "python"
indice_busqueda = mensaje.find(busqueda)
cantidad_caracteres_busqueda = len(busqueda)
resultado_busqueda = mensaje[indice_busqueda: (indice_busqueda + cantidad_caracteres_busqueda)]
print(busqueda, indice_busqueda, cantidad_caracteres_busqueda, " => ", resultado_busqueda)

# .startsWith(texto)  retorna un boolean si el caracter/string empieza por el texto
print("El mensaje empieza por %s" % (busqueda) + ' => ', mensaje.startswith(busqueda))
# .endWith(texto)  retorna un boolean si el caracter/string finaliza por el texto
print("El mensaje finaliza por %s" % (busqueda) + ' => ', mensaje.endswith(busqueda))
