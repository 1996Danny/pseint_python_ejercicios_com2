import datetime
import math
# from math import sqrt, pow
# from math import *


def calcular_raiz_2(n):
    res = math.sqrt(n)
    return res

# raiz = calcular_raiz_2(25)
# print(raiz)

# raiz_cuadrada = math.sqrt(81)

# print(f"El resultado de la raiz es: {raiz_cuadrada}")


fecha_actual = datetime.datetime.now()
fecha_actual2 = datetime.date.today()

# print(fecha_actual)
# print(fecha_actual2)


import random as rd

lista = ["daniel", "angelica", "segio", "rodrigo"]

ganador = rd.choices(lista)

print(ganador)


# TAREA: SOLICITAR AL USUARIO FECHA (AAAA:MM:dd)
# COMPLETA DE NACIEMIENTO 
# Y DEVOLVER LA EDAD