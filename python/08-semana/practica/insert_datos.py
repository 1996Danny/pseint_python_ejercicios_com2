
from conexion_db import conexion
from mysql.connector import Error

try:
    con = conexion()
    print("Conexion establecida..")
    cursor = con.cursor()

    # cursor.execute(
    #                 "insert into profesores(nombre, dni, direccion, telefono) values (%s,%s,%s,%s)", \
    #                 ("Ramon", "1243234", "Av. San Martin 1000", "53465436")
    #                 )

    insert = "insert into profesores(nombre, dni, direccion, telefono) values (%s,%s,%s,%s)"
    datos = [
        ("Ruben", "12435344", "Av. Güemes 2546", "675675"),
        ("Marcos", "54645667", "Catamarca", "4567657"),
    ]
    cursor.executemany(insert, datos)

    con.commit()

    print(f"Datos insertados: {cursor.rowcount}")

except Error as ex:
    print("Database error: ", ex)

finally:
    if con:
        con.close()
        print("Conexion cerrada...")