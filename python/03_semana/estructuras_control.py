

# continue: cuando la condicion se cumple "evita" y reanuda el bucle.

# for i in range(11):
#     if i == 5:
#         continue
#     print(f"iteración numero: {i}")

# print("Fin del programa")

# break: Cuadno la condicion se cumple se cierra el bucle.
# for i in range(11):
#     if i == 5:
#         break
#     print(f"iteración numero: {i}")

# print("Fin del programa")

# i = 0
# while i <= 10:
#     if i == 5:
#         i += 1
#         continue
#     print(f"iteracion numero: {i}")
#     i += 1


# i = 0
# while i <= 10:
#     if i == 5:
#         break
#     print(f"iteracion numero: {i}")
#     i += 1


# Condicionales

# si una persona puede votar o no. <= 16, si la ejemplar coincida con el dni

# edad = int(input("Ingrese la edad: "))
# ejemplar = input("El ejemplar del padron es igual al dni? ")

# if ejemplar == "si":
#     if edad >= 16:
#         print("Puede votar")
#     else:
#         print("no puede votar")
# else:
#     print("no puede votar")

        # v                   v
# if ejemplar == "si" and edad >= 16:
#     print("puede votar")
# else:
#     print("no puede votar")


# calificaciones agrupadas 1 a 5 (reprobado), 6 a 8(Bueno), 8 a 10 (excelente)

calificacion = int(input("Ingrese la calificacion: "))

if calificacion >= 1 and calificacion <= 5:
    print("Calificacion reprobado")

elif calificacion >= 6 and calificacion <= 8:
    print("Calificacion buena")

elif calificacion >= 9 and calificacion <= 10:
    print("Calificacion excelente")

else:
    print("Error")


