# 1-Crear un Personaje

class Personaje:
    poder_global = 100  # Atributo de clase y que es comparitdo por todos.

    # Tomando la línea 98: (p1, 200, "Sonic", "Erizo", 100)
    def __init__(self, fuerza, nombre, raza, vida):
        self.fuerza = fuerza
        # variable privada --> sólo va a ser accesible desde la misma clase.
        self.__nombre = nombre
        self._raza = raza  # variable protegida
        self._vida = vida  # variable protegida

    # Funcionalidades o comportamientos del Personaje
    def presentarse(self):
        print(f"Hola! Soy {self.__nombre}, de la raza {self._raza}")

    # Función para atacar
    def atacar(self, objetivo):
        daño = self.fuerza // 10  # El daño es proporcional a la fuerza
        print(
            f"{self.__nombre} ataca a {objetivo.__nombre} causando {daño} puntos de daño.")
        objetivo.defender(daño)
    # Función para defender

    def defender(self, daño_recibido):
        defensa = self.fuerza // 20  # Defensa reduce parte del daño
        daño_final = max(daño_recibido - defensa, 0)
        self._vida -= daño_final
        print(f"{self.__nombre} se defiende y recibe {daño_final} puntos de daño. Vida restante: {self._vida}")
        if self._vida <= 0:
            print(f"{self.__nombre} ha sido derrotado.")

    def get_nombre(self):
        return self.__nombre

    def set_fuerza(self, nueva_fuerza):
        if nueva_fuerza < 0:
            print("La fuerza no puede ser negativa.")
        else:
            self.fuerza = nueva_fuerza

    def __str__(self):
        return f"Personaje: {self.__nombre}, Raza: {self._raza}, Vida: {self._vida}, Fuerza: {self.fuerza}"


# Clases Hijas - Polimorfismo
class Guerrero(Personaje):
    def atacar(self, objetivo):
        print(f"{self.get_nombre()} lanza un golpe con espada!")
        # Ejecuta la función "ATACAR" de la clase padre (línea18).
        super().atacar(objetivo)


class Mago(Personaje):
    # Si no se coloca una función INITI, se utiliza el constructor de la clase padre (Personaje)
    def atacar(self, objetivo):
        print(f"{self.get_nombre()} lanza un hechizo mágico!")
        super().atacar(objetivo)

# Clases Herencia Multiple


class Volador:
    def volar(self):
        print("¡Estoy volando!")


class Curador:
    def curar(self, aliado):
        print(f"Curando a {aliado.get_nombre()}")


# Creo un Personaje que sea Mago, Volador y Curador
class MagoVolador(Mago, Volador, Curador):
    # Si no coloco la función INIT se utiliza el constructor de la clase padre (Mago), pero como Mago no tiene constructor, Python continúa la herencia hacia el abuelo (Personaje)
    # Sobreescribiendo el constructor.
    def __init__(self, fuerza, nombre, raza, vida, altura_max):
        Mago.__init__(self, fuerza, nombre, raza, vida)  # Llamo al constructor
        self.altura_max = altura_max


def pelea_turno(pj1, pj2):
    print("\n--- Comienza la pelea ---")
    turno = 1
    while pj1._vida > 0 and pj2._vida > 0:
        print(f"\nTurno {turno}:")
        pj1.atacar(pj2)
        if pj2._vida <= 0:
            break
        pj2.atacar(pj1)
        turno += 1
    print("\n--- Fin de la pelea ---")
    ganador = pj1 if pj1._vida > 0 else pj2
    print(
        f"🏆 El ganador es {ganador.get_nombre()} con {ganador._vida} puntos de vida restantes.")


# cuando llamo a la clase a partir del nombre de la clase --> se le pasa un objeto p1
p1 = Personaje(200, "Sonic", "Erizo", 100)
p2 = Personaje(150, "Mario", "Humano", 100)
pGuerrero = Guerrero(400, "Causilius", "Romano", 100)
pMV = MagoVolador(500, "Houdini", "Humano", 100, 1000)
p1.presentarse()
p2.presentarse()
pGuerrero.presentarse()
pMV.presentarse()
pelea_turno(pMV, pGuerrero)
