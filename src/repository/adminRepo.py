import mysql.connector
from mysql.connector import Error

from src.entities.AuthorEntity import AuthorEntity
from src.entities.CollectionEntity import CollectionEntity
from src.entities.CategoryEntity import CategoryEntity
from src.entities.PublisherEntity import PublisherEntity
from src.entities.RoleEntity import RoleEntity


class AdminRepo:
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
# for authors
# select queries
    def select_all_authors():
        pass

        # query="""SELECT * FROM author WHERE author_name LIKE %s"""
        
        # try:
        #     cursor = self.conn.cursor(dictionary=True)
        #     cursor.execute(query, ('%' + author_name + '%',))
        #     authors = cursor.fetchall()
        #     return [AuthorEntity(id_author =authors["id_author"],
        #                          name = authors["name"],)author in authors]
        # except Error as e:
        #     print(f"Erreur lors de la récupération des auteurs : {e}")
        #     return []
        # finally:
        #     cursor.close()
        #     print("Connexion à la base de données fermée")
        pass
# create querie
    def create_author(self, author:AuthorEntity):
        query = """INSERT INTO `author`(`Name_Author`) VALUES (%s)"""
        
        value = (author.name,)
        print(value)
        try:
                cursor = self.conn.cursor()
                cursor.execute(query, value)
                self.conn.commit()
                print("auteur créé avec succès")
                return cursor.lastrowid
        except Error as e:
            print(f"Erreur lors de l'ajout du livre : {e}")
            return None
# update querie
    def update_author():
        pass

# delete querie
    def delete_author():
        pass
    
# for collection
    def create_collec(self, collection:CollectionEntity):
        query = """INSERT INTO `collection`(`Name_collection`) VALUES (%s)"""
        
        value = (collection.name,)
        try:
                cursor = self.conn.cursor()
                cursor.execute(query, value)
                self.conn.commit()
                print("collection créé avec succès")
                return cursor.lastrowid
        except Error as e:
            print(f"Erreur lors de l'ajout de la collection : {e}")
            return None

# for categories
    def create_cat(self, category:CategoryEntity):
        query = """INSERT INTO `category`(`Name_Category`) VALUES (%s)"""
        
        value = (category.name,)
        try:
                cursor = self.conn.cursor()
                cursor.execute(query, value)
                self.conn.commit()
                print("categorie créé avec succès")
                return cursor.lastrowid
        except Error as e:
            print(f"Erreur lors de l'ajout de la categorie : {e}")
            return None

# for publisher
    def create_pub(self, publisher:PublisherEntity):
        query = """INSERT INTO `publisher`(`Name_Publisher`) VALUES (%s)"""
        
        value = (publisher.name,)
        try:
                cursor = self.conn.cursor()
                cursor.execute(query, value)
                self.conn.commit()
                print("l'éditeur a été créé avec succès")
                return cursor.lastrowid
        except Error as e:
            print(f"Erreur lors de l'ajout de l'éditeur : {e}")
            return None

# for role
    def create_role(self, role:RoleEntity):
        query = """INSERT INTO `role`(`Role_name`) VALUES (%s)"""
        
        value = (role.name,)
        try:
                cursor = self.conn.cursor()
                cursor.execute(query, value)
                self.conn.commit()
                print("nouveau role créé avec succès")
                return cursor.lastrowid
        except Error as e:
            print(f"Erreur lors de l'ajout du role : {e}")
            return None