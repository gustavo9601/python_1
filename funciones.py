def suma(valor1, valor2):
    return valor1 + valor2


print('La sumatoria es ' + str(suma(1, 2)))


def mensaje(name=None):
    mensaje = "Hola {}, bienvenido al curso de PY3".format(name)
    return mensaje


print(mensaje("Gustavo"))


# Retprmamdp varops valores para poder ser recibidos
def variosParametros():
    return "Curso de Python", 3.6, "Avanzado"


# Alacenamiento multiple, a partir de la respuesta de una funcion
curso, version, nivel = variosParametros()


def crear_usuario(nombre, apellido, edad):
    return {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "nombre_completo": "{} {}".format(nombre, apellido)
    }


user1 = crear_usuario("Gustavo", "Marquez", edad=24)
print(user1)
print(user1['nombre'])
print(user1['edad'])
print(user1['nombre_completo'])


# Especificando al inico del parametro *, permite establecer que recibira n parametos y se almacenaran en una tupla
def nParametros(param_requerido, *args):
    suma = 0
    for param in args:
        suma += param
    return (param_requerido + str(suma))


print('nParametros(1,2,3,4,5500)', nParametros("Valor requerido", 1, 2, 3, 4, 5500, -300))


# Especificando ** al inicio del parametros, permite agrupar los elementos pasados en un diccionario
# al llamar la funcion es necesario, definir el nombre de variable y valor, ya que se usaran como llave - valor
def users(**kwargs):
    print(kwargs)


users(nombre="gustavo", apellido="marquez", edad=24)


# Permite recibir de todo tipo de parametros
def combinacionParametros(param1, param2="Test", *args, **kwargs):
    print(param1, param2, args, kwargs)


combinacionParametros(100, 'Otro', 4, 5, 6, 7, 8, 2000, curso='Python', version=3.0, modalidad='virtual')

"""
Comportamiento de variables fuera y dentro de funciones 
"""

animal = 'Leon'  # variable global


def mostrar_animal():
    animal = "Tigre"  # variable local
    print(animal)


mostrar_animal()
print(animal)


def mostar_animal_global():
    # con global variable  // permite acceder a la variable del entrono global y editar su valor o su acceso desde la funcion
    global animal
    animal = 'Guepardo'
    print(animal)


mostar_animal_global()
print(animal)

"""
Funciones anonimas lambda
"""


def centigrados_a_faenheit(grados):
    return grados * 1.8 + 32


funcion_variable = centigrados_a_faenheit(24)
print("funcion_variable", funcion_variable)

# Abreviando la funcion anterior en una lamda
# variable = lamda param1, param2: operacion
# return implicito sin necesaridad de definirilo
variable_funcion_lambda = lambda grados=0: grados * 1.8 + 32
resultado = variable_funcion_lambda(555)
print(resultado)
# al igual que una funcion soporta cualquier tipo de parametro
con_asteriscos = lambda *args, **kwargs: args[0] + kwargs.get('valor', 50)
print(con_asteriscos(1, 2, valor=100))

"""
Funcion map
permite aplicar una funcion sobre n items de un objeto iterable
"""


def cuadrado(numero):
    return numero * numero


lista = [2, 4, 6, 8]
# map(funcion que recibe parametro, objeto iterable)
resultado = map(cuadrado, lista)
# se debe convertir a list o tuple, para que visualice los datos ya que retorna un valor de memoria
print("El cuadrado para {}".format(lista), " = ", list(resultado))

# Usando una lamda para abreviar la funcion
# map(funcion lamda, objeto iterable)
cuadrado_lambda = map(lambda numero: numero * numero, lista)
print(list(cuadrado_lambda))

"""
Funciones anidadas
"""


def playlist(canciones):
    def reproducir():
        # nonlocal canciones   // de esta forma se cambia el acceso a local de la variable, y puede ser modificada
        for idx, cancion in enumerate(canciones):
            print(idx, "-", cancion)

    # dentro del entrono de la funcion se debe llamar las respectivas funciones hijas para ser ejecutadas
    reproducir()


canciones = ['track 1', 'track 2', 'track 3']
playlist(canciones)

"""
Clouseres en funciones

# generar o retornar dinamicamente otra funcion
"""


def mostrar_mensage(msg):
    msg = msg.title()

    def mostrar():
        print(msg)

    return mostrar


nuevo_mensaje = mostrar_mensage("Bienvenidos al curso de PY 3")
nuevo_mensaje()  # necesario llamar la variable que reserva la funcion con () para ejecutarse

"""
Usando decoradores para potenciar una funcion
modificar o adicionara acciones
"""


# a, b, c
# a(b) -> c

# a
# funcion que recibe por parametro otra funcion
def decorador(funcion):
    # pass # no hace nada, solo permite estar vacio el ciclo, condicional o funcion
    # c
    def nueva_funcion(*args, **kwargs):
        print("Podemos agregar codigo antes")
        resultado = funcion(*args, **kwargs)
        print("Podemos agregar codigo despues")
        return resultado

    return nueva_funcion


# b
# @nombre funcion, que decorara la funcion que este abajo
@decorador
def funcion_a_decorar():
    print("Esta es una funcion a decorar")


@decorador
def suma_dos_numeros(val1, val2):
    return val1 + val2


funcion_a_decorar()

suma_resultado = suma_dos_numeros(1, 2)
print(suma_resultado)

"""
Generadores, => permite generar secuencias de datos para generar objetos iterables
"""


def tabla_multiplicar(numero, maximo=10):
    for posicion in range(1, maximo + 1):
        # yield es un return, que devolvera el valor, pero permitira la ejcucion del siguiente codigo
        yield numero * posicion, numero, posicion


print("lista_tabla_multiplicar", list(tabla_multiplicar(5, 15)))

# para este caso recorremos una funcion, qe devolvera un objeto iterable lista, de varias tuplas
for valor, numero, posicion in tabla_multiplicar(5, 15):
    print(str(numero) + " x " + str(posicion) + " = " + str(valor))
