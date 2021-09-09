import mysql.connector 

class mysql: 
    
    def __init__(self):
        self.connection = mysql.connector.connect (host = "localhost", user = "root", password = "gbm123", database = "bd1") 
        self.cursor = connection.cursor()
        
        query = ("SELECT nombre, apellido, email from form")
        
        self.cursor.execute (query)
        for (nombre, apellido, email) in cursor:
            print (query)   
        self.cursor.close()
        self.connection.close()