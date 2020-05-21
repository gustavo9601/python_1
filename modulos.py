# modulo => archivo dew py que permiten se rexpuesto s a otros

"""Documentación del módulo.
Esta es una anotación la cual debe de encontrarse
en la parte superior de nuestro script.
Esta anotación tiene cómo objetivo describir el módulo"""
__author__ = "Gustavo Marquez"
__copyright__ = "Copyright 2020, Gustavo M"
__credits__ = ["GM", "keyforb"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Team keyforb"
__email__ = "gustavomp@keyforb.com"
__status__ = "Production"


def suma(val1, val2):
    return val1 + val2


def resta(val1, val2):
    return val1 - val2


def multiplicar(val1, val2):
    return val1 * val2


def dividir(val1, val2):
    return "Division invalida a 0" if val1 == 0 else val1 / val2


# la variable __name__ obtiene el nombre del arhivo en ejecucion o importado
if __name__ == '__main__':
    print("Se esta llamando el archivo como principal")
else:
    print("Se esta llamando como modulo en otro archivo")
