import mysql.connector 
from mysql.connector import Error

def get_sql():
    try: 
        connection=mysql.connector.connect(
        host = "localhost",
        user = "user",
        passwrord = "password",
        database = "rohandb"
    )
    except Error as e:
        print(f"Error: {e}")
    



