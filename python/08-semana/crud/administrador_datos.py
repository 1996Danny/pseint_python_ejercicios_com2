
from conexion_db import get_connection
from mysql.connector import Error

# read
def obtener_empleados():
    con = get_connection()
    registros = []

    if con:
        try:
            cursor = con.cursor()
            print("Conexión establecida...")

            cursor.execute("SELECT * FROM empleados")
            registros = cursor.fetchall()
        except Error as ex:
            print("Error: ", ex)

        finally:
            con.close()

    return registros


# empleados = obtener_empleados()
# # print(empleados)
# for i in empleados:
#     print(f"ID: {i[0]}, Nombre: {i[1]}, Apellido: {i[2]}, Salario: {i[3]}, Cargo: {i[4]}, Tel: {i[5]}, Email: {i[6]}")


# create -> insert
def crear_empleados(dato_a_insertar):
    con = get_connection()

    filas_affected = 0

    if con:
        try:
            cursor = con.cursor()
            print("Conexión establecida...")

            query_insert = "INSERT INTO empleados(nombre, apellido, salario, cargo, telefono, correo) VALUES (%s, %s, %s, %s, %s, %s)"
            
            cursor.executemany(query_insert, dato_a_insertar)

            con.commit()

            filas_affected = cursor.rowcount

        except Error as ex:
            print("Error: ", ex)
            con.rollback
        finally:
            con.close()

    return f"La cantidad de registros insertados a la Base de Datos fue: {filas_affected}"


# update
def actualizar_empleados(id, nombre, apellido, salario, cargo, telefono, correo):
        con = get_connection()

        if con:
            try:
                cursor = con.cursor()

                query_update = "UPDATE empleados SET nombre = %s, apellido = %s, salario = %s, cargo = %s, telefono = %s, correo = %s WHERE id = %s"

                cursor.execute(query_update, (nombre, apellido, salario, cargo, telefono, correo, id))

                con.commit()

            except Error as ex:
                print("Error ", ex)
                con.rollback()

            finally:
                con.close()


# delete
def eliminar_empleados(id_empleado):
    con = get_connection()

    if con:
        try:
            cursor = con.cursor()

            query_update = "DELETE FROM empleados WHERE id = %s"

            cursor.execute(query_update, (id_empleado,))

            con.commit()

        except Error as ex:
            print("Error: ", ex)
            con.rollback()

        finally:
            con.close()

