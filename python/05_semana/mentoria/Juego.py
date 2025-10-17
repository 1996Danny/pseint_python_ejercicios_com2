# 1-Crear un Personaje

class Personaje:
    poder_global = 100  # Atributo de clase y que es comparitdo por todos.

    def __init__(self, fuerza, nombre, raza, vida):
        self.fuerza = fuerza
        self.nombre = nombre
        self.raza = raza
        self.vida = vida

    # Funcionalidades o comportamientos del Personaje
    def presentarse(self):
        print(f"Hola! Soy {self.nombre}, de la raza {self.raza}")

    # Función para atacar
    # Función para defender

# Pelea (Turno)
# p1 ataca a p2
# p2 ataca a p1


p1 = Personaje(200, "Sonic", "Erizo", 100)
p2 = Personaje(150, "Mario", "Humano", 100)
p1.presentarse()
p2.presentarse()
