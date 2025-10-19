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
    def atacar(self, objetivo):
        daño = self.fuerza // 10  # El daño es proporcional a la fuerza
        print(
            f"{self.nombre} ataca a {objetivo.nombre} causando {daño} puntos de daño.")
        objetivo.defender(daño)
    # Función para defender

    def defender(self, daño_recibido):
        defensa = self.fuerza // 20  # Defensa reduce parte del daño
        daño_final = max(daño_recibido - defensa, 0)
        self.vida -= daño_final
        print(f"{self.nombre} se defiende y recibe {daño_final} puntos de daño. Vida restante: {self.vida}")
        if self.vida <= 0:
            print(f"{self.nombre} ha sido derrotado.")

# Pelea (Turno)
# p1 ataca a p2
# p2 ataca a p1


def pelea_turno(pj1, pj2):
    print("\n--- Comienza la pelea ---")
    turno = 1
    while pj1.vida > 0 and pj2.vida > 0:
        print(f"\nTurno {turno}:")
        pj1.atacar(pj2)
        if pj2.vida <= 0:
            break
        pj2.atacar(pj1)
        turno += 1
    print("\n--- Fin de la pelea ---")
    ganador = pj1 if pj1.vida > 0 else pj2
    print(
        f"🏆 El ganador es {ganador.nombre} con {ganador.vida} puntos de vida restantes.")


p1 = Personaje(200, "Sonic", "Erizo", 100)
p2 = Personaje(150, "Mario", "Humano", 100)
p1.presentarse()
p2.presentarse()
pelea_turno(p1, p2)
