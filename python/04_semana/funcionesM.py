"""
# Sin función
# print("Bienvenido, Rafael")
# print("Bienvenido, Lucía")

# Con función
def saludar(nombre):
    print("Hola ", nombre)


def division(a, b):
    # print("Bienvenido,", nombre)
    print("calculando...")
    if b == 0:
        return False
    return a / b


# a = suma() + suma(5, 8)
# a =   9      +   13
# print(a)
# Parametro : Son las variables que se definen en la declaración de la función.
# Argumento : El valor que le paso a la función en el llamdo.
resultado = division(9, 0)
if (resultado):
    print("El resultado es:", resultado)
else:
    print("Ha intentado realizar una división por 0")

#variable global 
final = 0
def precio_final(precio, dif):
    iva = 1.21
    iva_dif = 1.105
    if dif:
        final = precio * iva_dif
    else:
        final = precio * iva
    return final
#la función precio_final va a tener el valor de la variable "final" definida DENTRO de la función y la variable final al terminar de ejecutarse la función desaparece.

print(final)

print("El precio final a abonar es: ", precio_final(100, True))
"""
"""
# utilizando listas


# Python me pide que las variables que tengan un valor por defecto, estén despues que las variables que no lo tienen.
def contar_altos(minimo, lista=[]):
    contador = 0
    for item in lista:
        if item > minimo:
            contador += 1
    return contador


edades = [5, 12, 18, 7, 3, 25, 40, 8]
mayores = contar_altos(12, edades)  # llamado por valor
mayores2 = contar_altos(minimo=12, lista=edades)  # llamado por parámetro
print("Hay", mayores, "edades mayores a ", 12)
"""
# ARGS


# el asterisco convierte los valores que le pasen a la función cuando se la llama en una tupla
def sumar_precios(*precios):
    total = 0
    for precio in precios:
        total += precio
    return total


print("Total: ", sumar_precios(100, 250, 300, 50))

# kwargs


# el doble asterisco convierte los valores que le pasen a la función cuando se la llama en un diccionario
def mostrar_datos(**datos):
    for clave, valor in datos.items():
        print(clave, ":", valor)


# => {"nobmre":"Rafael", "edad":44, "profesion":"Programador"}
mostrar_datos(nombre="Rafael", edad=44, profesion="Programador")
