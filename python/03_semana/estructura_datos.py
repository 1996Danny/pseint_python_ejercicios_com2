
var1 = 1
var2 = 2
var3 = 3


# estructuras de datos
    # listas (arrays, secuencia, ...) / Ordenadas y Mutables
    # indefinida "cant. elementos" y en "tipo de dato"

# lista vacia
# lista = list()
# lista = []
# # print(type(lista))
# #                                    -2    -1
# #        0  1    2        3      4    5     6
# lista = [1, 2, "Hola", [1, 4], None, 1.2, True]
# # lista = [1, 2, "Hola", None, 1.2, True]
# # print(type(lista), lista)

# # elemento al indice indicado
# print(lista[2])
# print(lista[5])
# # print(lista[10])
# # elementos 1 a 3
# print(lista[1:4])
# # ultimo elemto
# print(lista[-1])
# # inverso
# print(lista[::-1])

# metodos

lista_nombres = []

# agrega el valor dado al final de lista
lista_nombres.append("Dani")
lista_nombres.append("Alejandro")
lista_nombres.append("Flavia")
lista_nombres.append("Irrito")

# print(lista_nombres)

# elimina los elementos de una lista
# lista_nombres.clear()
# cuenta la cant de veces que aparece el valor dentro de la lista
# a = lista_nombres.count("Dani")
# print(a)

# si no se pasa el indice se elimina el ultimo elemento
# lista_nombres.pop()

# devuelve el primer elemento que coincide con el valor dado
# a = lista_nombres.index("Alejandro")
# print(a)
# print(lista_nombres)

# len() devuelve la longitud de la lista
# a = len(lista_nombres)
# print(len(lista_nombres))

# elimina el valora dado
# remove(x)

# extend([1,4,5])

# ordenar los elementos de la lista
# lista_numeros = [9,5,2,7,90]
# lista_numeros.sort(reverse=True)
# print(lista_numeros)

# ------------------------------------------------------------------------------------

# Tuplas son ordenadas, no son mutables

# tupla = tuple()
# tupla = ("dani", "frias")

# nombre, apellido = tupla

# print(nombre, apellido)

# print(type(tupla), tupla)

# tupla = (1,4,"hola", 1, 5 ,1 ,6 ,1)

# # print(tupla.count(1))
# # print(tupla.index("hola"))

# # print(tupla[2:5])
# # print(tupla[2])
# # print(tupla[-1])
# print(len(tupla))
# print(tupla)

# ----------------------------------------------------------------

# sets - conjuntos No ordenadas, Mutables
#  {}
# no tenemos indices / no se repiten elementos
# conjunto = set()
# conjunto = set([1,1,1,2,5,"hola", "mundo", "hola"])

# conjunto.add("Hola mundo")
# conjunto.remove(1)

# # print(type(conjunto))
# print(conjunto)


# --------------------------------------------------------------------

# Diccionarios Ordenados, solo el valor es mutable. clave-valor

# diccionario = dict()

diccionario = {}

# print(type(diccionario), diccionario)

# diccionario = {
#     "1": 2,
#     "nombre": "Daniel", 
#     "apellido": "Frias",
#     "lista": [
#         1,2,4,6,
#     ]
#     }

# print(diccionario)

# diccionario["nombre"] = "Dani"

# print(diccionario)

# a = diccionario.get("lista2")
# print(a)
# a = diccionario.get("lista")
# print(a)

# print(diccionario.keys()) # es un vista/view, secuencia de claves
# print(diccionario.values()) # es un vista/view, secuencia de valores
# print(diccionario.items()) # es un vista/view, secuencia de clave-valor

# diccionario["direccion"] = "Av. 25 de mayo 20000"

# print(diccionario)

# diccionario.pop("direccion")
# print(diccionario)