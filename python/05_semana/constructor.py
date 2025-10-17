
class Coche:
    # ruedas = 4 # atr de clase
    # constructor o inicializador (metodos magicos o dunder methods)
    def __init__(self, marca, modelo):
        self.marca = marca #atr de instancia
        self.modelo = modelo #atr de instancia

coche1 = Coche("Toyota", "Hilux")
# print(coche1.ruedas)
coche2 = Coche("ford", "ranger")
coche3 = Coche("toyota", "tacoma")
coche4 = Coche("ford", "territory")
coche5 = Coche("chevrolet", "tracker")

print(coche1.marca)
print(coche1.modelo)
print(coche2.marca)
print(coche2.modelo)
print(coche3.marca)
print(coche3.modelo)
print(coche4.modelo)
print(coche4.marca)
