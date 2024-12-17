
import mysql.connector

def db_connexion():
    try:
        conn = mysql.connector.connect(
            host="localhost",          
            user="userLibrary",   
            password="qazwsx00",
            database="library_python"
        )
        if conn.is_connected():
            print("Connexion réussie à la base de données")
        return conn
    except mysql.connector.Error as e:
        print("Erreur de connexion:", e)
        return None

