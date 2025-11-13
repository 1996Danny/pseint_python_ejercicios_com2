import mysql.connector

# host = "localhost" # 127.0.0.1
# port = "3306"
# user = "root"
# password = "1234"
# database = "instituto_db"

def conexion():
    return(mysql.connector.connect(
        host = "localhost",
        port = "3306",
        user = "root",
        password = "1234",
        database = "instituto_db"
    ))

