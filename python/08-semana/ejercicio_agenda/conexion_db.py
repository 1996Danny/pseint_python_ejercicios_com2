import mysql.connector

def conexion():
    return(mysql.connector.connect(
        host = "localhost",
        port = "3306",
        user = "root",
        password = "1234",
        database = "agenda_db"
    ))

# - Añadir contacto
# con = conexion()
# print("conexion establecida")
# cursor = con.cursor()
# cursor.execute(
#                 "insert into agenda(nombre, apellido, telefono, email) values (%s,%s,%s,%s)", \
#                 ("Ramon", "Perez", "12423523", "ramon@perez.com")
#                 )

# con.commit()

# print(f"Datos insertados: {cursor.rowcount}")

# con.close()

# - Borrar contacto ()
# con = conexion()
# print("conexion establecida")
# cursor = con.cursor()
# cursor.execute("delete from agenda where=3")
# con.commit()
# print(f"Datos elimindas: {cursor.rowcount}")
# con.close()

# - Listar contactos(todos los contactos)
# select * from contactos

# - Buscar contacto (por id, nombre) con id=5
# select * from contacto where id=5

# - Editar contacto ()

# con = conexion()
# print("conexion establecida")
# cursor = con.cursor()
# cursor.execute("update agenda set nombre='Ramiro' where id=2")
# con.commit()

# # print(f"Datos insertados: {cursor.rowcount}")
# con.close()