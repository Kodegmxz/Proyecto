from .envread import db_User, db_Host, db_Password, db_DB
import mysql.connector
from mysql.connector import Error

'''
class DataB:
    def __init__(self,host_a,user_a,password_a,database_a):  # Constructor que inicia la db
        try:
            self.db = mysql.connector.connect(
                host=host_a,
                user=user_a,
                password=password_a,
                database=database_a
            )
            self.dbcursor = self.db.cursor()
            self.status=True
            print("Exito al conectar")
        except mysql.connector.Error as err:
            print(f"Error al conectar a la base de datos: {err}")
'''
class DataB:
    def __init__(self):
        self.db = None
        self.dbcursor = None
    def connect(self):
        try:
            self.db = mysql.connector.connect(
                host=db_Host,
                user=db_User,
                password=db_Password,
                database=db_DB
            )
            self.dbcursor = self.db.cursor()
            return True
        except Error as err:
            return False
