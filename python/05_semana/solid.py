

# 1- SRP (cada clase de realizar una unica tarea)

# no se aplica SRP
# class Barbaro:
#     def __init__(self, nombre):
#         self.nombre = nombre

#     def atacar():
#         pass

#     def calcular_danio():
#         pass

#     def aumentar_progreso():
#         pass


# Logica de ataque del personaje
class Barbaro:
    def __init__(self, nombre):
        self.nombre = nombre

    def atacar(self):
        return(f"{self.nombre} (Barbaro) ataca con furia")

# Calculo de daño
class CalcularDanio:
    def calcular(danio_base, nivel):
        return f"daño: ",danio_base * (nivel)
    
# Datos
class Datos:
    def guardar_progreso(personaje, nivel):
        print(f"Se guarda el progreso del {personaje} nivel: {nivel}")


barbaro1 = Barbaro("Thrall")
danio_base = 5
nivel_actual = 10

print(barbaro1.atacar())
print(CalcularDanio.calcular(danio_base, nivel_actual))

Datos.guardar_progreso(barbaro1.nombre, 11)
