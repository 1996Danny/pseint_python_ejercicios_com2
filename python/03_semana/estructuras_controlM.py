"""
¿cuándo usamos decisiones y repeticiones en la vida real?

Ejemplos cotidianos:

    Si el precio supera cierto valor → aplicar descuento.

    Recorrer lista de productos para mostrar los que están en stock.

"""
"""
# iterable (que el algoritmo lo puede recorrer) cualquier estructura de datos (listas, tuplas, diccionarios, cadenas de texto)
texto = "Hola mundo"  # cadena de texto (string)

# .  "indice".   "iterable"
for caracter in texto:  # (H,o,l,a, ,m,u)
    # for i in range(10): # (0,1,2,3,4,5,6,7,8,9)
    print(caracter)
"""
"""
# Recorrer lista de precios > a 50000:
precios = [30000, 75000, 120000, 45000]  # lista -> es iterable

for precio in precios:  # por cada pasada que haga el "for" la variable precio va a tomar el valor de la posción de la lista correspondiente
    if precio > 50000:
     print(precio)

print("hola")     
#pasada 1:
# precio = 30000 ???? 30000 > 50000? false ----> entonces no ejecuta la impresión
# pasada 2:
# precio = 75000 ???? 75000 > 50000? true ----> entonces ejecuta la impresión
# pasada 3:
# precio = 120000 ???? 120000 > 50000? true ----> entonces ejecuta la impresión
# pasada 4:
# precio = 45000 ???? 45000 > 50000? false ----> entonces no ejecuta la impresión
"""
"""
# Cargar productos hasta ingresar "fin":
productos = []  # lista vacia
producto = ""  # variable vacia


while producto != "fin":
    producto = input("Ingrese un producto - o ingrese fin para terminar")
    if producto != "fin":
        productos.append(producto)  # agrego el producto a la lista
    else:
        # primera manera de mostrar
        print(f"La lista de productos es: {productos}")
        # segunda manera de mostrar
        print("Esta es la lista de productos:")
        for producto in productos:
            print(f"<> - {producto}")
        # Si el programa entra en "else" significa que -producto = "fin"-, por lo tanto "while producto != "fin"" va a ser falso, y se termina el bucle.
        break


"""
"""
    1-Ficha de producto con control de stock - imprimir si el producto tiene un stock bajo: --DICCIONARIO--
    2-Crear una lista que contiene 5 diccionarios, cada uno representando un producto. Recorrer la lista y mostrar solo los productos con stock menor a 5.
💡      Bonus: mostrar cuántos cumplen la condición.
"""
