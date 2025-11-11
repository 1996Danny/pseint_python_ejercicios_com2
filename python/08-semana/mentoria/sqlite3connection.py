import sqlite3
conn = sqlite3.connect("text.db")
""" conn.execute('''
CREATE TABLE PERSONA (
    ID INT PRIMARY KEY NOT NULL,
    NOMBRE TEXT NOT NULL,
    EDAD INT NOT NULL,
    DIRECCION CHAR(50)
);
''') """

""" conn.execute("INSERT INTO PERSONA VALUES (1, 'Pablo', 32, 'Av. Chaco 123')")
conn.execute("INSERT INTO PERSONA VALUES (2, 'Ana', 25, 'Av. Nueva 123')")
conn.commit()
 """

""" conn.execute('''
  UPDATE PERSONA SET DIRECCION = "Calle 3" WHERE ID = 2
''')
conn.commit() """

""" cursor = conn.execute("SELECT ID, NOMBRE, EDAD, DIRECCION FROM PERSONA")
for row in cursor:
    print(row)
 """
