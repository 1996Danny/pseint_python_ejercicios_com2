
# clase (plantilla, molde...) convencion PascalCase

class Persona:
    # atributos - caracteristicas(altura, color, nombre)
    edad = "20" # atr de clase
    nombre = "Juan" # atr de clase
    apellido = "Perez" # atr de clase

    # metodos - comportamientos (mover, saltar, saludar)
    # self es una referencia a la instancia
    def saludar(self):
        print("Hola!")

# instancia
pers1 = Persona()
pers2 = Persona()
pers3 = Persona()
pers4 = Persona()
pers5 = Persona()

# mostrar los atributos de Persona
print(pers1.nombre)
print(pers1.apellido)
print(pers2.edad)
print(pers2.nombre)
print(pers2.apellido)
print(pers3.edad)
print(pers3.nombre)
print(pers3.apellido)
print(pers1.edad)
print(pers1.nombre)
print(pers1.apellido)
print(pers1.edad)

# llamada al metodo
pers1.saludar()
