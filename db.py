from xmlrpc.client import Boolean
import mysql.connector

class Database:
    """Database MySQL"""
    def __init__(self,username="root",password="temp",host="localhost",port=8806,database="pms"):
        self.connection = None
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        print(username)

    def create_connection(self):
        """Create Connection for MySQL"""
        self.connection = None
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.username,
                passwd=self.password,
                port=self.port,
                database=self.database
            )
            print(self.connection.is_connected())
            print("Connection to MySQL DB successful")
        except mysql.connector.Error as err:
            print(f"The error '{err}' occurred")

    def is_connected(self) -> bool:
        """Return if Database is Connected"""
        return self.connection.is_connected()
    
    def run_query(self,query):
        """Run Query"""
        with self.connection.cursor() as cursor:
            cursor.execute(query)
        return cursor.fetchall()
    
    def run_sp(self,sp_name,sp_parameters=None):
        """Run a Store Proceedure"""
        return None
