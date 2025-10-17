# Personaje de un video juego.
# caracteristicas o propiedaes
# funcionalidad o comportamiento

# Producto de un supermercado
# producto --> diccionario
""" producto = {
    name: "pan",
    price: 1000,
    stock: 20
} """

# Progrmación orientada a objetos:


class Producto:  # MOLDE
    # Atributo que va a ser "Igual" en todos los objetos.
    id = 0

    # Atributos o propiedades
    # Constructor --> Genera un objeto por cada vez que yo llame a la función INIT
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    # Métodos o funcionalidades
    def vender(self, cantidad):
        if cantidad > self.stock:
            print("No hay suficiente stock")
        else:
            self.stock -= cantidad
            print(f"Se han vendido {cantidad} unidades de {self.name}")

    def reponer(self, cantidad):
        self.stock += cantidad
        print(f"Se han repuesto {cantidad} unidades de {self.name}")

    # Se usa para funciones que no modifiquen las propiedades del objeto ni de la clase. Función de Clase
    @staticmethod
    def enVidriera():
        print(f"Producto en vidriera")


class Auto:
    ruedas = 4

    def __init__(self, marca, modelo, color="Azul"):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def modificarRuedas():
        Auto.ruedas = 5


"""
    # Forma correcta:
    @classmethod
    def cambiarRuedas(cls):
        cls.ruedas = 5
"""

# Objeto o Instancias
pan = Producto("Pan", 1000, 1000)
leche = Producto("Leche", 2000, 500)
queso = Producto("Queso", 10000, 200)
auto1 = Auto("Toyota", "yaris", "azul")
# auto1.ruedas = 5
# print(pan.id)
# print(leche.id)
# print(queso.id)
auto2 = Auto("Ford", "Renegade")
# Auto.modificarRuedas()

print(auto1.ruedas)
print(auto2.ruedas)
print(auto2.color)
pan.enVidriera()
