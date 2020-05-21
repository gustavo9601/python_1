
# import nombreModulo
# import nombreModulo as nombreOpcional
# from nombreModulo import * # de esta forma se llama la funcion directamente y no necesita nombreModulo.funcion
    # * hace referencia a todas las funciones, o pueden ser solo el nombre de la funcion o funciones separados por ,
# from nombreModulo import nombreFuncion as nuevoNombreFuncion
# from nombreModulo import (funcionUno, funcionDos, Funcion3)


import modulos as calculadora


suma = calculadora.suma(50,60)
division = calculadora.dividir(0,2)
print("Llamando funcion suma del archivo modulos = ", suma)
print("Llamando funcion division del archivo modulos = ", division)


# Premite imprimir los comentarios, nombres clases, funciones, atributos
help(calculadora)