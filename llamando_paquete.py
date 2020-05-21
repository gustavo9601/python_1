from paquete1.modulo1 import hablar
from paquete1 import Humano   # para este caso no es necesari especificair el modulo, ya que se importa en el __init__

# usa la funcion que esta en el modulo1 de paquete 1
print(hablar())

# usa la clase que esta en el modulo 2 de paquete 1
humano1 = Humano()
print(humano1.cuerpo())


