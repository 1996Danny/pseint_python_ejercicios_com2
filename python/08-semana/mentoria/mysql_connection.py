import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="newpassword",
    database="agenda_contactos"
)

cursor = conn.cursor()

# CREAR TABLA AGENDA
cursor.execute('''
    CREATE TABLE IF NOT EXISTS agenda (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(50) NOT NULL,
        apellido VARCHAR(50) NOT NULL,
        email VARCHAR(100) NOT NULL,
        telefono VARCHAR(20) NOT NULL
    )
''')


def agregar_contacto(nombre, apellido, email, telefono):
    cursor.execute('''
        INSERT INTO agenda (nombre, apellido, email, telefono) VALUES (%s, %s, %s, %s)
    ''', (nombre, apellido, email, telefono))
    conn.commit()


def editar_contacto(id, nuevo_telefono, nuevo_email):  # *args -no es conveniente usar-
    cursor.execute('''
        UPDATE agenda SET telefono = %s, email = %s WHERE id = %s
    ''', (nuevo_telefono, nuevo_email, id))
    conn.commit()


"""
    def editar_nombre(id, nuevo_nombre): #*args -no es conveniente usar-
    cursor.execute('''
        UPDATE agenda SET nombre = %s WHERE id = %s
    ''',(nuevo_nombre, id))
    conn.commit()
"""


def listar_contactos():
    cursor.execute('''
        SELECT * FROM agenda
    ''')
    contactos = cursor.fetchall()
    for contacto in contactos:
        print(contacto)


print("ingresar los datos al campo que desea modificar. Para no modificar presionar ENTER.")
name = input("Ingrese Nombre: ")
lastname = input("Ingrese Apellido: ")
mail = input("Ingrese email: ")
phone = input("Ingrese Número de Teléfono: ")

# agregar_contacto(name, lastname, mail, phone)
listar_contactos()
conn.close()
