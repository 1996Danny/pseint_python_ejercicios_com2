
import mysql.connector
from mysql.connector import Error

# CRUD: create, read, update, delete (ABM)

def get_connection():
    try:
        connection = mysql.connector.connect(
                    host = "localhost",
                    port = "3306",
                    user = "root",
                    password = "1234",
                    database = "empresa_db"
                )
        return connection
    except Error as ex:
        print("Error: ", ex)

