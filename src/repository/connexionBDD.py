
import mysql.connector

def db_connexion():
    try:
        conn = mysql.connector.connect(
            host="localhost",          
            user="root",   
            password="",
            database="biblio_python"
        )
        if conn.is_connected():
            print("Connexion réussie à la base de données")
        return conn
    except mysql.connector.Error as e:
        print("Erreur de connexion:", e)
        return None

