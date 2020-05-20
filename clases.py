class Usuario:
    pass
    # todas las funciones dentro de una clase, deben recibir un parametro
    # por convencion se coloca self, pero puede ser cualquier nombre, y este idnicara que es un metodo de clase
    def saludar(self, nombre):
        print("Holaaa ", nombre , " que tal ?")


user1 = Usuario()
user2 = Usuario()

# type(objeto) => devuleve de que tipo es el objeto de instancia de la clase
print(type(user1))
user1.saludar("Gustavo")
