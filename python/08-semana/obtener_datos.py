
from conexion_db import conexion
from mysql.connector import Error

# try ejecuta una accion. si da error pasa bloque except. 
# finally siempre se ejecuta al final.

try:
    con = conexion()
    print("Conexion establecida..")

    cursor = con.cursor()

    cursor.execute("select * from profesores")

    # registros = cursor.fetchone()
    registros = cursor.fetchall()

    print(registros)

except Error as ex:
    print("Database error: ", ex)

finally:
    if con:
        con.close()
        print("Conexion cerrada...")