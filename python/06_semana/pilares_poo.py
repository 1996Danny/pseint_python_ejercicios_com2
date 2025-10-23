
# Herencia, metodos y atributos desde una clasepadre/superclase/clasebase. clasehija/subclase

# clase padre
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def saludar(self):
        return "Hola"
        
# Herencia Simple
# clase hija
class Estudiante(Persona):
    def __init__(self, nombre, apellido, escuela):
        super().__init__(nombre, apellido)
        self.escuela = escuela

    def saludar(self):
        return "Hola desde clase estudiantes"


# per = Persona("Adrian", "Juarez")
# print(per.nombre)
# print(per.saludar())


# est = Estudiante("Juan", "Perez", "EEP 200")
# print(est.apellido)
# print(est.saludar())

# Herencia multiple, heredar met, atr de dos o mas clases.

class Mamifero:
    def __init__(self, nombre):
        self.nombre = nombre

    def presentar(self):
        return f"Hola soy {self.nombre} un mamifero"
    
    def caminar(self):
        return "Respiracion pulmonar"
    

class Pez:
    def __init__(self, nombre, aletas):
        self.nombre = nombre
        self.aletas = aletas
    
    def nadar(self):
        return "puedo nadar"
    
class Delfin(Mamifero,Pez):
    def __init__(self, nombre, aletas):
        super().__init__(nombre)
        Pez.__init__(self, nombre, aletas)

# delfin = Delfin("Delfi", "tiene aletas")

# print(delfin.presentar())
# print(delfin.nadar())
# print(delfin.caminar())

# print(Delfin.__mro__)


#  Polimorfismo (metodos iguales que realizan diferentes acciones)

class Animal:
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido():
        return "Guau!!"
    
class Gato(Animal):
    def hacer_sonido():
        return "Miau!!"



# perro = Perro.hacer_sonido()
# print(perro)

# gato = Gato.hacer_sonido()
# print(gato)

# Encapsulamiento (__Privado"se puede acceder desde dentro clase")
                # (_Protegido "accedeer desde la clase o clases hijos")
                # (Publicos "podemos accedes desde cualquie parte del codigo")

class CuentaBancaria:
    def __init__(self, saldo):
        # self.saldo = saldo # publico
        # self._saldo = saldo #protegido
        self.__saldo = saldo # privado
    
    # getter
    # def get_saldo(self):
    #     return f"Saldo: ${self.__saldo}"
    
    # setter
    # def set_saldo(self, nuevo_saldo):
    #     self.__saldo = nuevo_saldo



#     @property
#     def saldo(self):
#         return self.__saldo
    
#     @saldo.setter
#     def saldo(self, nuevo_saldo):
#         self.__saldo = nuevo_saldo


# cuenta1 = CuentaBancaria(600)
# cuenta1._saldo = 1000
# print(cuenta1._saldo)
# print(cuenta1.__saldo)
# cuenta1.__saldo = 1000

# print(cuenta1.get_saldo())

# cuenta1.set_saldo(1000)

# print(cuenta1.get_saldo())

# print(cuenta1.saldo)

# cuenta1.saldo = 1000

# print(cuenta1.saldo)



# Abstraccion (mostrar la informacion que esencial dentro de la clase)
            # las clases abstractas no son instanciables

from abc import ABC, abstractmethod

class Figuras(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass
    
    def mostrar_informacion(self):
        print ("Esto es una figura")


class Circulo(Figuras):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14 * self.radio ** 2
    
    def perimetro(self):
        return 2 * self.radio * 3.14

circ = Circulo(5)
print(f"Area del cilculo es {circ.area()}")
print(f"Area del cilculo es {circ.perimetro()}")


class Cuadrado(Figuras):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * 2

    def perimetro(self):
        return "!"

cuad = Cuadrado(2)

print(f"Area del cuadradop es {cuad.area()}")