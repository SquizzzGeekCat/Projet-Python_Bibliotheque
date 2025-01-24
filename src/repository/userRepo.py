import mysql.connector
from mysql.connector import Error

from src.entities.UserEntity import UserEntity


class UserRepo:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                port=3306,
                database="mylibrary",
                user="admin",
                password="qazwsx00"
                )
            if self.conn.is_connected():
                print("Connexion à la base de données réussie")
            else :
                print("Connexion à la base de données échouée")
        except mysql.connector.Error as e:
            print(f"Erreur lors de la connexion à la base de données : {e}")
            self.conn = None
            
    def create_user(self, user:UserEntity):
        query = """INSERT INTO `user_`(`Lastname`, `Firstname`, `Pseudo`, `Email`, `Password`, `Born_at`, `Statut`, `Id_Role`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
        values = (user.last_name,user.first_name,user.pseudo,user.email,user.password,user.date_birth,user.statut,3)
        
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, values)
            self.conn.commit()
            print(f"L'utilisateur {user.first_name} a été créé avec succès.")
            return cursor.lastrowid
        except Error as e:
            print(f"Erreur lors de l'ajout de l'utilisateur : {e}")
            return None
