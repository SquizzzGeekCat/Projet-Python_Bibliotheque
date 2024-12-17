from connexionBDD import db_connexion
import mysql.connector
from src.entities.BookBo import BookEntities
from mysql.connector import Error

class BookRepository:
    def __init__(self, host, database, user, password):
        try:
            self.connexion = mysql.connector.connect(
                host=host,
                user=user,
                port=3306,
                password=password,
                database=database
            )
            if self.connection.is_connected():
                print("Connexion à la base de données réussie")
            else :
                print("Connexion à la base de données échouée")
        except mysql.connector.Error as e:
            print(f"Erreur lors de la connexion à la base de données : {e}")
            self.connection = None
            
    # select type queries
    def select_all_book(self):
        query = "SELECT * FROM book"
        try:
            cursor = self.connexion.cursor(dictionary=True)
            cursor.execute(query)
            books = cursor.fetchall()
            return [BookEntities(
                book["id"],
                book["title"],
                book["author"],
                book["category"],
                book["publisher"],
                book["publication_date"],
                book["collection"],
                book["isbn"],
            )for book in books]
        except Error as e:
            print(f"Erreur lors de la récupération des livres : {e}")
            return []

    def select_book_by_id(self,id):
        pass
    def select_book_by_title(self,id):
        pass

    def select_book_by_author(self,author):
        pass

    def select_book_by_category(self,category):
        pass

    def select_book_by_publisher(self,publisher):
        pass

    def select_book_by_collection(self,collection):
        pass

    # create querie
    def insert_book(self,book):
        pass

    # update queries
    def update_book(self,id):
        pass

    def update_book_return_date(self,id, return_date):
        pass

    # archive queries
    def archive_book_by_id(self,id):
        pass
