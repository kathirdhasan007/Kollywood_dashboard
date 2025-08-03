import mysql.connector

#connect to database 

def get_connection():
    return mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "Kathir@123",
            database = "Dashboard"
    )