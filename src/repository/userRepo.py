import mysql.connector
import bcrypt
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

    def login(self, data:dict):
        query = """SELECT * FROM `user_` WHERE Email=%s"""
        values = (data["email"],)
        
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute(query, values)
            user = cursor.fetchone()
            if user:
                # Vérifier le mot de passe haché
                if bcrypt.checkpw(data["password"].encode('utf-8'), user["Password"].encode('utf-8')):
                    print(f"Connexion réussie pour l'utilisateur {user['Firstname']}")
                    return UserEntity(
                        user["Id_User"], user["Lastname"], user["Firstname"],
                        user["Pseudo"], user["Email"], user["Password"],
                        user["Born_at"], user["Statut"], user["Id_Role"]
                    )
                else:
                    print("Connexion échouée : mot de passe incorrect")
                    return None
            else:
                print("Connexion échouée : identifiants incorrects")
                return None
        except Error as e:
            print(f"Erreur lors de la connexion : {e}")
            return None
            
    def update_user(self, user):
        query = """UPDATE `user_` SET Lastname=%s, Firstname=%s, Pseudo=%s, Email=%s, Password=%s, Born_at=%s, Statut=%s, Id_Role=%s WHERE Id_persone=%s"""
        values = (user.last_name, user.first_name, user.pseudo, user.email, user.password, user.date_birth, user.statut, user.id_role, user.id_person)
        
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, values)
            self.conn.commit()
            print(f"L'utilisateur {user.first_name} a été mis à jour avec succès.")
        except Error as e:
            print(f"Erreur lors de la mise à jour de l'utilisateur : {e}")
    def select_all_users(self):
        query = """SELECT * FROM `user_`"""
        
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute(query)
            users = cursor.fetchall()
            return users
        except Error as e:
            print(f"Erreur lors de la récupération des utilisateurs : {e}")
            return []
    def get_user_by_id(self, user_id):
        query = """SELECT * FROM `user_` WHERE Id_persone=%s"""
        values = (user_id,)
        
        try:
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute(query, values)
            user = cursor.fetchone()
            if user:
                print(f"Utilisateur trouvé : {user}")
                return UserEntity(user["Id_persone"], user["Lastname"], user["Firstname"], user["Pseudo"], user["Email"], user["Password"], user["Born_at"], user["Statut"], user["Id_Role"])
            else:
                print("Utilisateur non trouvé")
                return None
        except Error as e:
            print(f"Erreur lors de la récupération de l'utilisateur : {e}")
            return None
                  
    def __del__(self):
        """
        Ferme la connexion à la base de données.
        """
        if self.conn and self.conn.is_connected():
            self.conn.close()
            print("Connexion à la base de données fermée")