# el nombre del archivo debe ser __init__.py para que python sepa que es un paquete(direcotiro) de modulos
from .modulo2 import Humano
# se ejecutara primero que cualquier archivo se instancie del paquete en relacion
print("Este es un mensaje del archivo __init__")

"""
Es usado como conexiones de BD, clases etc, instancias de alguna de las clases que tiene el paquete
"""