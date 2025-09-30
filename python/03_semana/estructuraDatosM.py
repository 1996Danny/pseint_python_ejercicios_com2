producto1 = ["Zapato", 1000, 10]  # lista
producto1[1] = 1500

listaSupermercado = ["Jabon", "Fideos", "Papel Higienico"]

# newItem = input("Ingrese el nombre del producto: ")

# listaSupermercado.append(newItem)

producto2 = ("Camisa", 2000, 5)  # tupla
persona = ("Juan", "Perez", 30)  # tupla
persona = ("Juan", "Perez", 35)  # tupla

ubicacionResistencia = (-27.45, -58.98)  # Resistencia, Chaco
# print("Latitud:", ubicacionResistencia[0])
# print("Longitud:", ubicacionResistencia[1])

diasDeLaSemana = ("Lunes", "Martes", "Miercoles",
                  "Jueves", "Viernes", "Sabado", "Domingo")

persona = {
    "nombre": "Juan",
    "apellido": "Perez",
    "edad": 30
}

productoZapato = {
    "nombre": "Zapato",
    "precio": 1200,
    "stock": 10
}


interesxtarjeta = 0.15

productoRemera = {
    "nombre": "Remera",
    "precio": {
        "efectivo": 1100,
        "tarjeta": {
            "debito": 1100 * interesxtarjeta,
            "credito": 1300
        }},
    "stock": 20
}

productos = [productoZapato, productoRemera]  # lista

# print(productoZapato.keys())

print(productos[1]["precio"]["tarjeta"]["debito"] * 10)
configuracion = {
    "idioma": "español",
    "moneda": "pesos",
    "tema": "claro"
}

configuracion["tema"] = "oscuro"

configuracion["notificaciones"] = True


if (configuracion["tema"] == "claro"):
    print("El tema es claro")
else:
    print("El tema es oscuro")

print(configuracion)
configuracion.pop("notificaciones")  # eliminar un par clave-valor
print(configuracion.pop("notificaciones", "No existe la clave"))
configuracion.clear()  # eliminar todos los pares clave-valor
# configuracion.popitem()  # eliminar el ultimo par clave-valor
# del configuracion["idioma"]  # eliminar un par clave-valor
print(configuracion)

Formato = (NombreCarrera, NumeroEstudiantes)
Ingenieria = ("Ingeniería Informática", 150)
Medicina = ("Medicina", 200)
Derecho = ("Derecho", 180)
