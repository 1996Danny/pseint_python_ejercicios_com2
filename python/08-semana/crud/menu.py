

from administrador_datos import crear_empleados, obtener_empleados, actualizar_empleados, eliminar_empleados

# dato_para_insertar = [
#                     ("Jose", "X", "2000", "front", "3456343","jose@x.com"),
#                     ("Mario", "Roibledo", "2000", "back", "67678875","mario@robledo.com")
#                       ]

# crear_empleados(dato_para_insertar)


# empleados = obtener_empleados()
# for i in empleados:
#     print(f"ID: {i[0]}, Nombre: {i[1]}, Apellido: {i[2]}, Salario: {i[3]}, Cargo: {i[4]}, Tel: {i[5]}, Email: {i[6]}")


# id_empleado = 14

# actualizar_empleados(
#     id_empleado,
#     "Mariaaa",
#     "Alcaraz",
#     "1500",
#     "Administrador",
#     "124233454",
#     "mariaaaa@alcaraz.com"
# )

# eliminar_empleados(15)


# Menu

while True:

    print("Bienvenidos Crud empresa")

    opcion = int(input("ingrese una opcion: "))

    if opcion == 1:
        empleados = obtener_empleados()
        for i in empleados:
            print(f"ID: {i[0]}, Nombre: {i[1]}, Apellido: {i[2]}, Salario: {i[3]}, Cargo: {i[4]}, Tel: {i[5]}, Email: {i[6]}")
    # opcion 2 insertar

    # opcion 3 modificar

    # opcion 4 eliminar

    # opcion 5 o O Salir
    # break