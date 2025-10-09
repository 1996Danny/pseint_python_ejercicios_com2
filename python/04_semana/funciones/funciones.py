
# funciones: un bloque de codigo, organizado y realiza una unica accion
    # Modularizar el codigo.
    # Reutilizacion

# definimos funcion sin parametros y no retorna nada
# def nombre_func():
#     print("Hola soy una función")


# # llamada/invocar
# nombre_func()

# funciones con parametros
def calcular_area_cuadrado(lado): # area_cuadrado = lado * lado
    area = lado * lado
    print(f"El area del cuadrado es: {area}")

# llamada con argumeto
# calcular_area_cuadrado(4)
# calcular_area_cuadrado(2)
# calcular_area_cuadrado(1)
# calcular_area_cuadrado(10)

def calcular_area_rectangulo(b, h): # area_rectangulo = b * h
    area = b * h
    print(f"El area del rectangulo es: {area}")

# calcular_area_rectangulo(2, 3)
# calcular_area_rectangulo(4, 8)

# ejemplo funcion returno nulo
# res = calcular_area_rectangulo(2, 3) + 5
# print(res)

# ===============================================================
# Tarea: hacer las funciones para triangulo, circulo
# Tarea: unificar todos los calculos de arear en un menu(c,r,t,cir)
# =====================================================================
# funciones con retorno

def calcular_area_rectangulo(b, h): # area_rectangulo = b * h
    area = b * h
    # print(f"El area del rectangulo es: {area}")
    return area

# llamada a la funcion con retorno y se asigna a variabloe area_rect
# area_rect = calcular_area_rectangulo(2, 3)
# print(f"area del rectangulo {area_rect}")

# funciones con parametros por defecto
# def saludar(momento_dia="dias"):
#     print(f"Buenos {momento_dia}")


# # saludar("dias")
# # saludar("tardes")
# saludar("noches")
# saludar()

# funciones con parametros indefinidos

# *args (a,3,5,6,7,6,)
def obtener_promedio(*numeros): # sumar todos los numeros y dividir x la cant
    suma = sum(numeros)
    longitud = len(numeros)
    promedio = suma / longitud

    print(promedio)

# obtener_promedio(5)
# obtener_promedio(5,5,5,6,10,10,1,8,4,5,3,2)
# obtener_promedio(5,5,5,6,10,10)
# obtener_promedio(5)
# obtener_promedio(5,5,5)
# obtener_promedio(5,5,5,6,10,10,1,8,4,5,3,2,7,7,7,7,7,7)
# obtener_promedio(5,5,5,6,10,10,1,8)

# **kwargs (clave=valor)

# def crear_perfil_usuario(nombre="usuario" , **kwargs):
#     print(nombre)
#     print("_____________________________________")

#     for clave, valor in kwargs.items():
#         print(f"{clave} : {valor}")

# crear_perfil_usuario("Daniel", apellido="Frias", edad=28, nac="20/6")
# crear_perfil_usuario("Daniel", apellido="Frias", edad=28, nac="20/6", direc="Belgrano 102", prov="Chaco")