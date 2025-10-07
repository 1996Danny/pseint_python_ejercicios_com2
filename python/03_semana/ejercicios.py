
# Ejercicios convinacion estructuras de control y de datos

# 1- Definir una "lista" de precios y aplica un 15% de descuento 
#   solo a los precios mayores a 10.00, y contar cuántas 
#   veces se aplicó el descuento.

productos = [50.00, 12.00, 8.50, 1.50, 22.00, 7.75, 3.00, 9.99, 1.15, 4.25]
descuento = 0.15 # .85
contador_descuento = 0
productos_con_descuento = []

for i in range(len(productos)):
    if productos[i] >= 10.00:
        print(f'el producto que se podria aplicar el descuento es:' ,productos[i])
        productos[i] = productos[i] *(descuento) # productos[i] -= productos[i] *(descuento)
        productos_con_descuento.append(productos[i])
        contador_descuento += 1

print(f'la cantidad de productos con descuento es: {contador_descuento}')
print(f'Los productos con descuento son:{productos_con_descuento}')


# 2- solicitar nombre, nota de estudiantes y agregar a un "diccionario". 
#   Iterar sobre las claves y valores de un diccionario para 
#   clasificar a los estudiantes en dos listas según su nota>7.




# 3- definir una "tupla" con posibles destinos(paises), 
#   buscar un destino en la tupla y, al encontrarlo, 
#   usa break para salir inmediatamente del bucle, optimizando la búsqueda.
#               0         1         2          3        4
destinos = ["Portugal", "China", "Mexico", "Japon", "Australia"]
pais = input("Ingrese el destino a verficar: ")

for destino in destinos:
    if destino == pais.capitalize():
        print(f"Su destino {pais} esta disponible!")
        break
    else:
        print(f"Buscando... Pais: {pais}")
else:
    print(f"Busqueda finalizado, no hubo coincidencias para {pais}")




# 4- Definir una "lista" de 10 numeros(0 al 10) 
#   usar continue para omitir cualquier valor igual a cero, 
#   asegurando que solo los valores positivos contribuyan a la suma 
#   y a la lista filtrada.



